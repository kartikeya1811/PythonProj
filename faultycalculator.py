num1 = input("Enter the first number:")
num2 = input("Enter the operator:")
num3 = input("Enter the second number:")

tot = num1 + num2 + num3

if tot == "45*3":
    print(555)
elif tot == "56+9":
    print(77)
elif tot == "56/6":
    print(4)
elif num2 == '*':
    print(int(num1)*int(num3))
