def reverse_text(text):
    return text[::-1]

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Error: Invalid operation"

if __name__ == "__main__":
    print("Choose a tool:")
    print("1. Text Reverser")
    print("2. Calculator")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        text = input("Enter text to reverse: ")
        print("Reversed text:", reverse_text(text))
    elif choice == '2':
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operation (+, -, *, /): ")
            result = calculator(a, b, op)
            print("Result:", result)
        except ValueError:
            print("Error: Invalid number input.")
    else:
        print("Invalid choice.")
