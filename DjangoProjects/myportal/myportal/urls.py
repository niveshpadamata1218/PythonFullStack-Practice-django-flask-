from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Add this import

def root_redirect(request):
    return redirect('/students/')  # Or 'student_list' if named

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root_redirect),  # Add this for root
    path('', include('myapp.urls')),  # Keep this
]
