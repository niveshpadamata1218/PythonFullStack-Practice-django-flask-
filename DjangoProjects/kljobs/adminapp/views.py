from django.shortcuts import render

# Create your views here.
def adminhomepage(request):
    return render(request,'adminapp/projecthomepage.html')
def printer(request):
    return render(request, 'adminapp/printer.html')
def timetable(request):
    return render(request,'adminapp/timetable.html')
