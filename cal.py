a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("choose an operator (+, -, *, /, **, mod): ") 
r = 0
if op == "+":
    r = a + b
    print(f"the result of {a} + {b} = {r}")
elif op == "-":
    r = a - b
    print(f"the result of {a} - {b} = {r}")
elif op == "*":
    r = a * b
    print(f"the result of {a} * {b} = {r}")
elif op == "/":
    r = a / b
    print(f"the result of {a} / {b} = {r}")
elif op == "**":
    r = a ** b
    print(f"the result of {a} ** {b} = {r}")
elif op == "mod":
    r = a % b
    print(f"the result of {a} mod {b} = {r}")
else:
    print("invalid operator")