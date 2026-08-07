print("===== Python Calculator =====")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. modulus")
print("6. power")

choice = input("Choose an operation (1, 2, 3, 4, 5, 6): ")

# Check if the choice is valid first
if choice in ("1", "2", "3", "4", "5", "6"):

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    if choice == "1":
        print("Addition =", first_number + second_number)

    elif choice == "2":
        result = first_number - second_number
        print("Subtraction =", result)

    elif choice == "3":
        result = first_number * second_number
        print("Multiplication =", result)

    elif choice == "4":
        if second_number != 0:
            result = first_number / second_number
            print("Division =", result)
        else:
            print("Error: Division by zero is not allowed.")

    elif choice == "5":
        print("Modulus =", first_number % second_number)

    elif choice == "6":
        print("Power =", first_number ** second_number)

else:
    print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")
