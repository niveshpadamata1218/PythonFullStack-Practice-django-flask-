from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'myapp/student_list.html', {'students': students})
