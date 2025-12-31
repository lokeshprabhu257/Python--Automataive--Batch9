# Decorator with wrapper and inner function + user input
def calculator(func):
    def wrapper(a, b):
        def inner():
            if func.__name__ == "add":
                return a + b

            elif func.__name__ == "subtract":
                return a - b

            elif func.__name__ == "multiply":
                return a * b

            elif func.__name__ == "divide":
                if b == 0:
                    return "Cannot divide by zero"
                return a / b

            else:
                return "Invalid operation"

        print("Result:", inner())

    return wrapper


@calculator
def add(a, b):
    pass


@calculator
def subtract(a, b):
    pass


@calculator
def multiply(a, b):
    pass


@calculator
def divide(a, b):
    pass


# -------- User Input --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nChoose operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

if choice == 1:
    add(a, b)
elif choice == 2:
    subtract(a, b)
elif choice == 3:
    multiply(a, b)
elif choice == 4:
    divide(a, b)
else:
    print("Invalid choice")
