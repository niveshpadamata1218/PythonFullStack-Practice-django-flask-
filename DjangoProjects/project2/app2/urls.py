from django.urls import path
from . import views

urlpatterns = [
    path('klu/', views.function2, name='function2'),
]