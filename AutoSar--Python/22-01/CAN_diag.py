import csv
import json
import argparse

# ==========================
# DBC mapping (simple)
# ==========================
DBC = {
    0x100: {
        "vehicle_speed": {"start": 0, "len": 16, "factor": 0.01},
        "engine_rpm": {"start": 16, "len": 16, "factor": 1},
        "steering_angle": {"start": 32, "len": 16, "factor": 0.1},
    }
}

# ==========================
# Diagnostic thresholds
# ==========================
MAX_SPEED_RATE = 50       # km/h per second
MAX_STEERING_RATE = 90    # deg per second
RPM_MIN, RPM_MAX = 0, 8000

# ==========================
# Helpers
# ==========================
def extract(data_int, start, length):
    return (data_int >> start) & ((1 << length) - 1)

# ==========================
# Main logic
# ==========================
def process_frames(csv_file, out_file):

    # ---- real-time state ----
    state = {
        "vehicle_speed": None,
        "engine_rpm": None,
        "steering_angle": None,
        "timestamp": None
    }

    with open(csv_file) as f, open(out_file, "w") as out:
        reader = csv.DictReader(f)

        for row in reader:
            ts = int(row["timestamp_ms"])
            can_id = int(row["can_id_hex"], 16)
            data = int.from_bytes(bytes.fromhex(row["data_hex"]), "little")

            if can_id not in DBC:
                continue

            # ---- decode signals ----
            decoded = {}
            for sig, cfg in DBC[can_id].items():
                raw = extract(data, cfg["start"], cfg["len"])
                decoded[sig] = raw * cfg["factor"]

            # ---- diagnostics (compare with previous state) ----
            if state["timestamp"] is not None:
                dt = (ts - state["timestamp"]) / 1000.0
                if dt > 0:
                    # speed jump
                    speed_rate = abs(decoded["vehicle_speed"] - state["vehicle_speed"]) / dt
                    if speed_rate > MAX_SPEED_RATE:
                        out.write(json.dumps({
                            "timestamp": ts,
                            "event": "SPEED_JUMP",
                            "rate": round(speed_rate, 2)
                        }) + "\n")

                    # steering jump
                    steering_rate = abs(decoded["steering_angle"] - state["steering_angle"]) / dt
                    if steering_rate > MAX_STEERING_RATE:
                        out.write(json.dumps({
                            "timestamp": ts,
                            "event": "STEERING_RATE_EXCEEDED",
                            "rate": round(steering_rate, 2)
                        }) + "\n")

            # RPM check
            if not (RPM_MIN <= decoded["engine_rpm"] <= RPM_MAX):
                out.write(json.dumps({
                    "timestamp": ts,
                    "event": "RPM_OUT_OF_RANGE",
                    "rpm": decoded["engine_rpm"]
                }) + "\n")

            # ---- update state (IMPORTANT) ----
            state.update(decoded)
            state["timestamp"] = ts

# ==========================
# CLI
# ==========================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Use safe variable names
    parser.add_argument("--input", default="frames.csv", help="Input CSV file")
    parser.add_argument("--output", default="events.jsonl", help="Output JSONL file")
    args = parser.parse_args()

    process_frames(args.input, args.output)
    print("Processing completed")