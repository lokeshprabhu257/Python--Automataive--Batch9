try:
    # Read length of list
    n = int(input("Enter the length of the list: "))

    # Check for non-negative length
    if n < 0:
        print("Error: The length of the list must be a non-negative integer.")
        exit()

    total = 0

    # Read list elements
    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        total += num

    # Calculate and print average
    if n > 0:
        average = total / n
        print("Average:", format(average, ".2f"))
    else:
        print("Average: 0.00")

except ValueError:
    # Handles non-numeric input for n or list elements
    print("Error: You must enter a numeric value.")
