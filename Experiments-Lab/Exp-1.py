# from operator import truediv
#
# number1=int(input("enter a number"))
# if number1>0:
#     print("number1 is positve ")
# elif number1<0:
#     print("number1 is  negative")
# else:
#     print("number1 is ZERO ")
#
# var1=2400030538
# var2="absd"
# var3=True
# var4=100
# var5='PRESENT'
# print(var1,"datatype",type(var1))
# print(var2,"datatype",type(var2))
# print(var3,"datatype",type(var3))
# print(var4,"datatype",type(var4))
# print(var5,"datatype",type(var5))
# var6=input("enter an input")
# print(var6,"datatype",type(var6))
from turtledemo.paint import switchupdown
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

while True:
    char = input("enter a character (+, -, *, q to quit): ")

    match char:
        case '+':
            print(num1 + num2, "addition")

        case '*':
            print(num1 * num2, "multiplication")

        case '-':
            print(num1 - num2, "subtraction")

        case 'q':
            print("Exiting program")
            break

        case _:
            print("Invalid operator")












