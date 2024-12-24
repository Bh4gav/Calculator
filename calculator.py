def calculator():
    print("Welcome to the Calculator! Let’s add some fun to math!")
    print("Type 'exit' to quit anytime.")
    while True:
        expression = input("\nEnter a math problem to solve (or type 'exit' to quit): ").strip()
        if expression.lower() == 'exit':
            print("Goodbye! Hope this calculator multiplied your joy!")
            break
        allowed_chars = "0123456789+-*/(). "
        if all(char in allowed_chars for char in expression):
            result = eval(expression)
            print(f"Result: {result}")
        else:
            print("Invalid input! Please enter a valid math expression using numbers and operators (+, -, *, /).")
calculator()
