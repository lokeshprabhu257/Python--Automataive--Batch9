#----1-----

DISCOUNT_RATE = 20
TOTAL_MEMBERS = 6


class MovieTicket:
    def _init_(self, name, age, ticket_price):
        self.name = name
        self.age = age
        self.ticket_price = ticket_price

    def is_senior_citizen(self):
        if self.age >= 60:
            return True
        else:
            return False

    def calculate_discount(self):
        discount = (self.ticket_price * DISCOUNT_RATE) / 100
        return discount 
    
#-----2------

    def calculate_final_price(self):
        if self.is_senior_citizen():
            final_price = self.ticket_price - self.calculate_discount()
            return final_price
        else:
            return self.ticket_price

    def display_ticket_details(self):
        print("\n------------------------------")
        print("Ticket Details")
        print("------------------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Senior Citizen:", self.is_senior_citizen())
        print("Original Ticket Price:", self.ticket_price)

        if self.is_senior_citizen():
            print("Discount Applied:", self.calculate_discount())
        else:
            print("Discount Applied: 0")

        print("Final Ticket Price:", self.calculate_final_price())
        print("------------------------------")

#-----3------

try:
    total_amount = 0

    print("\n WELCOME TO MOVIE TICKET DISCOUNT SYSTEM ")
    print("Senior Citizen Discount:", DISCOUNT_RATE, "%")
    print("Total Members:", TOTAL_MEMBERS)

    for i in range(1, TOTAL_MEMBERS + 1):
        print(f"\nEnter details for Member {i}")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        ticket_price = float(input("Enter Ticket Price: "))

        ticket = MovieTicket(name, age, ticket_price)
        ticket.display_ticket_details()

        total_amount = total_amount + ticket.calculate_final_price()

    average_price = total_amount / TOTAL_MEMBERS

    print("\n===================================")
    print("GROUP BOOKING SUMMARY")
    print("===================================")
    print("Total Members:", TOTAL_MEMBERS)
    print("Total Amount to Pay:", total_amount)
    print("Average Ticket Price:", average_price)
    print("===================================")

except ValueError:
    print("\nError: Invalid input! Please enter numeric values.")

except Exception as e:
    print("\nUnexpected Error Occurred:", e)

finally:
    print("\nBooking process completed successfully.")
    print("Thank you for using the Movie Ticket Discount System ")