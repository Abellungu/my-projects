def main():
    print("== Simple Calculator ==")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Choose operator (+, -, *, /): ")
            num2 = float(input("Enter secondnumber: "))
            if operator == "+":
                print("Result:", num1 + num2)
            elif operator == "-":
                    print("Result:", num1 - num2)
            elif operator == "*":
                        print ("Result:", num1 * num2)
            elif operator ==  "/":
                if num2 != 0:
                    print("Result:", num1 / num2)
                else:
                     print("Error: Cannot divide by zero")
            else:
                print("Invalid operator")
        except ValueError:
            print("Please enter valid numbers")
        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() != "yes":
            print("Goodbye")
            break
main()
