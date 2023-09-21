"""
URL configuration for indra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.BasePageView.as_view(), name='base_page'),
    path('admin/', admin.site.urls), # Admin login 
    path('console/', include('console.urls')),  # Include the "console" app's URLs
    path('user/', include('User.urls')),  # Include the "User" app's URLs
    path('technician/', include('technician.urls')),  # Include the "technician" app's URLs
    path('api/', include('console.api_urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('', include('user.urls', namespace='user')),
    # Add other app-specific URLs here if needed
]



