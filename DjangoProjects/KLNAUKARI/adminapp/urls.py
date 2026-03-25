from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin_home'),
    path('printer/', views.printer, name='printer'),
    path('printer/add/', views.timetable, name='timetable'),
    path('time1/', views.time1, name='time1'),
    path('signup/', views.signup, name='signup'),
path('login/', views.login_view, name='login'),
]
