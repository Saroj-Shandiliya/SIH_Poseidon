# technician/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('technician-login/', views.technician_login, name='technician_login'),
    # Other app-specific URLs
]