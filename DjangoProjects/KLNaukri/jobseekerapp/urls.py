from django.urls import path
from . import views
urlpatterns = [
    path('jobseekerhomepage/',views.jobseekerapp,name='jobseekerapp'),
]