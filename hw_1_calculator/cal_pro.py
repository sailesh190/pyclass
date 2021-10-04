# code for calulator

operation_keywords = ["ADD", "MUL", "SUB", "DIV"]

def operation_fun(a, b, operation_type):
    if operation_type == "ADD":
        return f"Output for {a} + {b} = {a + b}"
    elif operation_type == "MUL":
        return f"Output for {a} * {b} = {a * b}"
    elif operation_type == "SUB":
        return f"Output for {a} - {b} = {a - b}"
    elif operation_type == "DIV":
        return f"Output for {a} / {b} = {a / b}"

if_continue = "Y"

while if_continue.upper() == "Y":
    
    operation_type = input("What calculation you want to perform? " + " ".join(operation_keywords) + ":")
    
    while operation_type.upper() not in operation_keywords:
        operation_type = input("You entered wrong operation, please enter " + " ".join(operation_keywords) + ":")

    a = int(input("Enter a value:"))
    b = int(input("Enter b value:"))

    print(operation_fun(a, b, operation_type.upper()))
    
    if_continue = input("Would you like to continue? (Y or N):")
    
    while if_continue.upper() != "Y" and if_continue.upper() != "N":
        if_continue = input("You entered wrong response. Would you like to continue? (Y or N):")