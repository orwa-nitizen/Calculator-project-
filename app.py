from calculator import add, subtract, multiply, divide

def menu():
    while True:
        print("
Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            elif choice == "4":
                result = divide(a, b)
            else:
                print("Invalid choice")
                continue

            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    menu()
