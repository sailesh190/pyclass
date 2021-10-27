calculate_oper = ["ADD","SUB","MUL","DIV"]

def calculate_fun(a,b,oper):
    if oper == "ADD":
        print( a+b)
    elif oper == "SUB":
        print( a-b)
    elif oper == "MUL":
        print( a*b)
    elif oper == "DIV":
        print( a/b)
    else:
        print('Err! Input operation is not in {}'.format(calculate_oper))

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = input("Enter Operation in {}".format(calculate_oper)).upper()
#c = raw_input("Enter Operation in {}".format(calculate_oper)).upper()

calculate_fun(a,b,c)