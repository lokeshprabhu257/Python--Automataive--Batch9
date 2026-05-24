from datetime import datetime, timedelta
import os

FILE_NAME = "key_log.txt"
MAX_HOURS = 2  # allowed key holding time


def take_key():
    if os.path.exists(FILE_NAME):
        print("Key is already taken.")
        return

    name = input("Enter employee name: ")
    time_now = datetime.now()

    with open(FILE_NAME, "w") as file:
        file.write(f"{name},{time_now}")

    print("Key recorded successfully.")


def show_current_holder():
    if not os.path.exists(FILE_NAME):
        print("Key is currently available.")
        return

    with open(FILE_NAME, "r") as file:
        name, time_str = file.read().split(",")

    taken_time = datetime.fromisoformat(time_str)
    print(f"🔑 Key is with: {name}")
    print(f"⏰ Taken at: {taken_time}")


def check_alert():
    if not os.path.exists(FILE_NAME):
        print("No alerts. Key is available.")
        return

    with open(FILE_NAME, "r") as file:
        name, time_str = file.read().split(",")

    taken_time = datetime.fromisoformat(time_str)
    if datetime.now() > taken_time + timedelta(hours=MAX_HOURS):
        print(f"ALERT: {name} has not returned the key on time!")
    else:
        print("Key is within allowed time.")


def return_key():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("Key returned successfully.")
    else:
        print("No key record found.")

def show_full_history():
    if not os.path.exists(FILE_NAME):
        print("No key records found.")
        return

    print("\n--- Key Holding Records ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, time_str = line.strip().split(",")
            taken_time = datetime.fromisoformat(time_str)
            print(f"Name: {name}, Taken at: {taken_time}")
    

def menu():
    while True:
        print("\n--- Office Key Tracker ---")
        print("1. Take Key")
        print("2. Show Current Holder")
        print("3. Check Alert")
        print("4. Return Key")
        print("5. Show Key Holding Records")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            take_key()
        elif choice == "2":
            show_current_holder()
        elif choice == "3":
            check_alert()
        elif choice == "4":
            return_key()
        elif choice == "5":
            show_full_history()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


menu()
