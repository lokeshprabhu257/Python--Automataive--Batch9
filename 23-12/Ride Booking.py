#  Ride classes 

class Ride:
    def __init__(self, distance):
        self.distance = distance 

    def calculate_fare(self):
        return 0.0   # default / base


#inherited classes
class MiniRide(Ride):
    def calculate_fare(self):
        base_fare = 30
        per_km = 8
        return base_fare + per_km * self.distance


class SedanRide(Ride):
    def calculate_fare(self):
        base_fare = 50
        per_km = 10
        return base_fare + per_km * self.distance


class SUVRide(Ride):
    def calculate_fare(self):
        base_fare = 80
        per_km = 13
        return base_fare + per_km * self.distance



#-------------------------------2---------------------------------
def show_fare(ride: Ride, ride_name: str):
    fare = ride.calculate_fare()          
    print(f"\n{ride_name} ride for {ride.distance} km will cost: ₹{fare}\n")


def main():
    print("=== Ride Booking Application ===")
    print("1. Mini Ride")
    print("2. Sedan Ride")
    print("3. SUV Ride")

    choice = input("Enter your choice (1-3): ")

    try:
        distance = float(input("Enter distance in km: "))
    except ValueError:
        print("Invalid distance! Please enter a numeric value.")
        return

    ride = None
    ride_name = ""

    if choice == "1":
        ride = MiniRide(distance)
        ride_name = "Mini"
    elif choice == "2":
        ride = SedanRide(distance)
        ride_name = "Sedan"
    elif choice == "3":
        ride = SUVRide(distance)
        ride_name = "SUV"
    else:
        print("Invalid choice!")
        return

    # Use base type reference (Ride) to show polymorphism
    show_fare(ride, ride_name)


# Run the program
if __name__ == "__main__":
    main()