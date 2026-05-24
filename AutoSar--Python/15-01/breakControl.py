import os

SAFE_TEMPERATURE = 100   

# CAN ID Mapping 
CAN_ID_MAP = {
    "0x100": "VehicleSpeed",
    "0x200": "EngineRPM",
    "0x300": "CoolantTemp"
}

# 2  MCAL Layer (File Access)

def read_can_log(file_path):
    if not os.path.exists(file_path):
        print(" Error: CAN log file not found!")
        return []

    with open(file_path, "r") as file:
        return file.readlines()


# Basic Software Layer

def decode_can_message(line):
    try:
        can_id, value = line.strip().split(",")
        signal = CAN_ID_MAP.get(can_id, "Unknown")
        return signal, int(value)
    except:
        return None, None


# 3       RTE (Run Time Environment)

def rte_transmit(signal, value):
    if signal == "VehicleSpeed":
        application_vehicle_speed(value)
    elif signal == "EngineRPM":
        application_engine_rpm(value)
    elif signal == "CoolantTemp":
        application_coolant_temp(value)



# Application Layer

def application_vehicle_speed(speed):
    print(f" Vehicle Speed: {speed} km/h")

def application_engine_rpm(rpm):
    print(f"Engine RPM: {rpm} rpm")

def application_coolant_temp(temp):
    print(f" Coolant Temperature: {temp} °C")
    if temp > SAFE_TEMPERATURE:
        print(" WARNING: Engine Overheating!")


#4            Main Program 
def main():
    print("\n===== CAN Bus Message Analyzer Started =====\n")

    file_path = os.path.join(os.getcwd(), "can_log.csv")

    can_data = read_can_log(file_path)

    if not can_data:
        return

    for message in can_data:
        signal, value = decode_can_message(message)
        if signal:
            rte_transmit(signal, value)


main()