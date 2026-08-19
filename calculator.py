# calculator.py
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else "Error"

print("Simple Calculator")
a = float(input("Enter first number: "))
op = input("Enter operator + - * /: ")
b = float(input("Enter second number: "))

if op == "+": print(add(a,b))
elif op == "-": print(sub(a,b))
elif op == "*": print(mul(a,b))
elif op == "/": print(div(a,b))
else: print("Invalid operator")