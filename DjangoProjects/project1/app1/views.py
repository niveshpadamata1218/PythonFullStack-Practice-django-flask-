from django.shortcuts import render
from django.http import HttpResponse
def function1(request):
    return HttpResponse("<font color='blue'>Welcome to Django</font>")
