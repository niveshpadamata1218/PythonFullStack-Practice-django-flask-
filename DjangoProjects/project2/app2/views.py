from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def function(request):
    return HttpResponse("<font color='green'> welcome to pfsd-django class")
def function2(request):
    return render(request, "HelloWorld.html")
