from django.urls import path
from . import views

urlpatterns=[
    path('',views.adminhomepage,name='adminhomepage'),
    path('printer/',views.printer,name='printer'),
    path('timetable',views.timetable,name='timetable')
]

