from django.shortcuts import render

# Create your views here.
def jobseekerapp(request):
    return render(request,'jobseekerapp/jobseekerhomepage.html')