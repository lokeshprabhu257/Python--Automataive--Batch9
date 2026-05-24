# ATM Simulator Application

class ATMError(Exception):
    pass

class InsufficientFundsError(ATMError):
    pass

class AuthenticationError(ATMError):
    pass

class CardNotFoundError(ATMError):
    pass

# Sample user data
users = {
    "1234567890": {"pin": "1234", "balance": 5000, "transactions": []},
    "9876543210": {"pin": "4321", "balance": 10000, "transactions": []}
}

def validate_card(card_number):
    if card_number not in users:
        raise CardNotFoundError("Card not found.")
    return True

def validate_pin(card_number, pin):
    if users[card_number]["pin"] != pin:
        raise AuthenticationError("Incorrect PIN.")
    return True

def check_balance(card_number):
    balance = users[card_number]["balance"]
    print(f"Your current balance is: ${balance}")
    users[card_number]["transactions"].append(f"Balance Inquiry: ${balance}")

def withdraw_cash(card_number, amount):
    if amount > users[card_number]["balance"]:
        raise InsufficientFundsError("Insufficient balance.")
    users[card_number]["balance"] -= amount
    print(f"Please collect your cash: ${amount}")
    users[card_number]["transactions"].append(f"Withdrawal: ${amount}")

def transaction_history(card_number):
    print("Transaction History:")
    for t in users[card_number]["transactions"]:
        print(f"- {t}")

def atm_menu(card_number):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Transaction History")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        try:
            if choice == "1":
                check_balance(card_number)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                withdraw_cash(card_number, amount)
            elif choice == "3":
                transaction_history(card_number)
            elif choice == "4":
                print("Thank you for using ATM.")
                break
            else:
                print("Invalid choice. Try again.")
        except ATMError as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Enter numeric values.")

# Main program
def main():
    print("--- Welcome to ATM Simulator ---")
    card_number = input("Enter card number: ")
    pin = input("Enter PIN: ")
    
    try:
        validate_card(card_number)
        validate_pin(card_number, pin)
        print("Authentication successful!")
        atm_menu(card_number)
    except ATMError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()