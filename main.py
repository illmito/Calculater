from logo import logo

print(logo)
#  Function for calculator. + - * /
# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# function with calculating code.
def calculator():
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calc_function = operations[operations_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculation with "
                 f"{answer}, or type 'N' to exit: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
