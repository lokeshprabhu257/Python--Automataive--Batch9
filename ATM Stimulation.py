# ATM Machine Simulation Program
            #1st 
print(" : Card inserted :")           # Show message that card is inserted
pin = input(" enter your pin:")       

if len(pin) != 4:                     # Check if PIN is exactly 4 characters
    print(" Invalid pin")             
    exit()                            

            #2nd 
balance = 1000                        # Starting account balance

def check_balance():                  # Function to show current balance
    print("Your balance is:", balance)  # Print balance on screen

             #3rd
def deposit():                        # Function to deposit money
    global balance                    # Use the global balance variable
    amount = input("Enter amount to deposit: ")  

    if amount.isdigit():              # Check that input has only digits
        amount = int(amount)          
        balance = balance + amount    
        print("Amount deposited successfully:", amount)  # Confirm deposit
        print("Current balance is:", balance)           
    else:
        print("Invalid amount. Numbers only.") 

             #4th 
def withdraw():                       # Function to withdraw money
    global balance                    # Use the global balance variable
    amount = input("Enter amount to withdraw: ")  # Take withdrawal amount

    if amount.isdigit():              # Check that input has only digits
        amount = int(amount)          
        if amount <= balance:         
            balance = balance - amount  
            print("Amount withdrawn successfully:", amount)  
            print("Current balance is:", balance)            
        else:
            print("Insufficient balance.")  
    else:
        print("Invalid amount. Numbers only.")  
           
                #5th 

while True:                           # Main loop to keep ATM running
    print("\n--- ATM MENU ---")      # Show menu header
    print("1. Check Balance")        
    print("2. Deposit Money")       
    print("3. Withdraw Money")       
    print("4. Exit")                 
    
                   #6th        
    choice = input("Enter your choice: ")  # Read user menu choice

    if choice == '1':               
        check_balance()              
    elif choice == '2':             
        deposit()                   
    elif choice == '3':             
        withdraw()                   
    elif choice == '4':             
        print("Thank you for using ATM.")  # Exit message
        break                        # Break loop and end program
    else:
        print("Invalid choice. Please try again.")  # Wrong menu input