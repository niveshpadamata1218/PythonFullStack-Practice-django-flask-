'''
a1=[1,2,3,4,"klu","klu2"]
a2={1,2,3,4,"klu","klu2"}
a3={1,2,3,4,"klu","klu2"}
a4={1:"nivesh",2:"nivesh2"}

fruits=["nivesh","nicky","hello"]
for fruit in fruits:
    print(fruit)

n=5
for i in range(0,n):
    for j in range(0,i):
        print(i,end=" ")
    print("\n")


count=0
while count<5:
    count=count+1

print(count)
'''
from itertools import count

# for cls in range(1,3):
#     print("class: ",cls)
#     for student in range(1,4):
#         print("student roll: ",student)

# for roll in range(1,6):
#     if roll==5:
#         break
#     print(roll)


# s = "nivesh"
# vowels = "aeiouAEIOU"
# count=0
# for ch in s:
#     if ch in vowels:
#         count=count+1
#
# print(count)
#
# name=123
# name=name[::-1]
# print(name)

#
# import math
# b=int(input("Enter a number: "))
# c=math.sqrt(b)
# d=math.ceil(b)
# print(c)
# print(d)

# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# c=a*b
# n=1
# while n<=c:
#     if(n%a==0 and n%b==0):
#         print(n,"lcm")
#         break
#     else:
#         n=n+1

