# #3.1
# import math
# from math import factorial
# num=5
# print(factorial((num)))
# #3.2
# def a():
#     print("hello a")
#     def b():
#         print("heloo b")
#     b()
# a()
# #3.3
# class A:
#     print("hello")
#     def function(self):
#         print("heloo");
#     def __init__(self):
#         print("how r you")
# my_obj=A()
# my_obj.function()
# #3.4
# class Parent:
#     def display(self):
#         print("i am a parent")
# class Child(Parent):
#     def childdisplay1(self):
#         print("iam child")
# class Child2(Parent):
#     def childdisplay2(self):
#         print("i am a child3")
# class Child3(Parent):
#     def childdisplay3(self):
#         print("i am a child3")
# p : Parent
# p=Child()
# p.display()

#multiple inheritance
class Sports:
    def __init__(self ,name):
        self.name=name
class Games:
    def __init__(self,gameName):
        self.gameName=gameName
class SportsGames:
    def __init__(self,exp,name,gameName):
        self.exp = exp
        Sports.__init__(self,name)
        Games.__init__(self,gameName)
        def display(self):
            print("fname:",{self.name},"fname:",self.gameName,"fname:",self.exp)

if __name__=="__main__":
    my_obj=SportsGames("Sports","Sports","Sports")
    my_obj.display()




