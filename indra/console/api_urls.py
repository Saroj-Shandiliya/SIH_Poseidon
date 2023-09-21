# console/api_urls.py
from django.urls import path
from .api_views import get_classified_data
from .import views
urlpatterns = [
    path('classified-data/', get_classified_data, name='classified-data'),
    # path('console-login/', views.console_login, name='console-login'),
    # Add more API endpoints as needed
]
