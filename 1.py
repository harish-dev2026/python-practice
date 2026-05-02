a = int(input("a="))
b = int(input("b="))
operation = input("add, sub, mul, div: ")

if (operation == "add"):
    print(a + b)
elif (operation == "sub"):
    print(a - b)
elif (operation == "mul"):
    print(a * b)
elif (operation == "div"):
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("invalid operator")
