from django.shortcuts import render, redirect
from .models import Employerdeatils


def employerhomepage(request):
    return render(request, 'employer/employerhomepage.html')


def crudfunction(request):
    return render(request, 'employer/crud.html')


def crud_insert(request):
    if request.method == "POST":
        empid = request.POST.get('empid')
        empname = request.POST.get('empname')
        emploc = request.POST.get('emploc')
        empphone = request.POST.get('empphone')
        empmail = request.POST.get('empmail')

        add = Employerdeatils(
            empid=empid,
            empname=empname,
            emploc=emploc,
            empphone=empphone,
            empmail=empmail
        )
        add.save()

        return redirect('crudfunction')   # ✅ fixed

    return redirect('crudfunction')
