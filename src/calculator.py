def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")

    choice = input("Choose an operation (1 or 2): ")

    if choice not in ("1", "2"):
        print("Invalid choice.")
        return

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if choice == "1":
        print("Result:", num1 + num2)
    else:
        print("Result:", num1 - num2)


calculator()

# This is for sample text addition