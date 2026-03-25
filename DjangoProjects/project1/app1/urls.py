from django.urls import path
from . import views
urlpatterns = [
    path('klu/',views.function1,name='function1'),
]
