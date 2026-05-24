import csv
from pathlib import Path
import can

SPEED_MIN = 0
SPEED_MAX = 200
CAN_ID_SPEED = 0x123
ROOT = Path(__file__).resolve().parent


# -----------------------------------
# FakeBus (Simple Simulation)
# -----------------------------------
class FakeCar:
    def __init__(self):
        self.messages = []

    def send(self, msg):
        self.messages.append(msg)

    def recv(self, timeout=1.0):
        if len(self.messages) > 0:
            return self.messages.pop(0)
        return None


# -----------------------------------
# Validate Speed
# -----------------------------------
def validate_speed_value(speed):
    return SPEED_MIN <= speed <= SPEED_MAX


# -----------------------------------
# Encode Speed
# -----------------------------------
def encode_speed(speed):
    if not validate_speed_value(speed):
        raise ValueError("Speed out of range")
    return speed.to_bytes(2, "big")


# -----------------------------------
# Decode Speed
# -----------------------------------
def decode_speed(data):
    if len(data) < 2:
        raise ValueError("Invalid data")
    return int.from_bytes(data[:2], "big")


# -----------------------------------
# Create Bus
# -----------------------------------
def create_bus(use_real_can=True):
    if use_real_can:
        return can.interface.Bus(
            bustype="virtual",
            channel="vcan0",
            receive_own_messages=True
        )
    else:
        return FakeCar()


# -----------------------------------
# Build Speed Message
# -----------------------------------
def build_speed_message(speed):
    data = encode_speed(speed)

    message = can.Message(
        arbitration_id=CAN_ID_SPEED,
        data=data,
        is_extended_id=False
    )

    return message


# -----------------------------------
# Send Speed
# -----------------------------------
def send_speed(bus, speed):
    msg = build_speed_message(speed)
    bus.send(msg)


# -----------------------------------
# Receive Speed
# -----------------------------------
def receive_speed(bus, timeout=1.0):
    msg = bus.recv(timeout=timeout)

    if msg is None:
        return None

    return decode_speed(msg.data)


# -----------------------------------
# Run Validation
# -----------------------------------
def run_validation_sequence(bus, speeds, timeout=1.0):
    results = []

    for speed in speeds:

        if not validate_speed_value(speed):
            results.append({
                "speed_kmh": speed,
                "expected": "0-200",
                "actual": "out_of_range",
                "status": "FAIL"
            })
            continue

        send_speed(bus, speed)
        received = receive_speed(bus, timeout)

        if received == speed:
            status = "PASS"
        else:
            status = "FAIL"

        results.append({
            "speed_kmh": speed,
            "expected": speed,
            "actual": received,
            "status": status
        })

    return results


# -----------------------------------
# Write CSV Report
# -----------------------------------
def write_csv_report(results, path):
    fieldnames = ["speed_kmh", "expected", "actual", "status"]

    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


# -----------------------------------
# Parse Speeds
# -----------------------------------
def parse_speeds(raw):
    speeds = []

    for item in raw.split(","):
        item = item.strip()
        if item:
            speeds.append(int(item))

    return speeds


# -----------------------------------
# Manual Sequence
# -----------------------------------
def manual_sequence(bus):
    results = []

    print("Enter speed value (q to quit)")

    while True:
        value = input("Speed: ")

        if value.lower() == "q":
            break

        try:
            speed = int(value)
        except:
            print("Invalid number")
            continue

        result = run_validation_sequence(bus, [speed])[0]
        results.append(result)

        print("Status:", result["status"])

    return results

if __name__ == "__main__":
    bus = create_bus(use_real_can=False)
    speeds = [0, 50, 100, 150, 200, 250]
    results = run_validation_sequence(bus, speeds)
    write_csv_report(results, "test_report.csv")
    print("CSV file created.")
