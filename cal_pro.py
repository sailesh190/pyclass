# code for calulator

# add
# mul
# sub
# div
operation_keywords = "ADD MUL SUB DIV"

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a/b


operation_type = input(f"What calculation you want to perform? {operation_keywords}:")

a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

if operation_type.upper() == "ADD":
    print(f"Output for {a} + {b} =", add(a, b))
elif operation_type.upper() == "MUL":
    print(f"Output for {a} * {b} =", mul(a, b))
elif operation_type.upper() == "SUB":
    print(f"Output for {a} - {b} =", sub(a, b))
elif operation_type.upper() == "DIV":
    print(f"Output for {a} / {b} =", div(a, b))
else:
    print(f"You entered wrong operation, please enter {operation_keywords}")