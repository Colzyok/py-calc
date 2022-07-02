num1 = float(input("Enter a numer: "))
op = input("Choose an operator: ")
num2 = float(input("Enter another numer: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
elif op == "**":
    print(num1 ** num2)
elif op == "%":
    print(num1 % num2)
else:
    print("Invalid operator, please try again.")