from django.urls import path
from . import views

urlpatterns = [
    path('employerhomepage/', views.employerhomepage, name='employerhomepage'),
    path('crudfunction/', views.crudfunction, name='crudfunction'),
    path('insert/', views.crud_insert, name='crud_insert'),
]
