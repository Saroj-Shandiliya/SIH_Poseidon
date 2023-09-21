# console/urls.py
from django.urls import path
from .api_views import check_authentication
from . import views
from . import api_views

urlpatterns = [
    path('console-login/', views.console_login, name='console_login'),
    path('console-dashboard/', views.console_dashboard, name='console_dashboard'),
    path('demo/', views.demo, name='demo'),
    path('classified-data/', views.classified_data_view, name='classified_data'),
    # path('demo/', views.classified_data_view, name='classified_data'),
    path('generate_report/', views.generate_report, name='generate_report'),
    path('generate_pie_chart/', views.generate_pie_chart, name='generate_pie_chart'),
    path('generate_outgoing_flow_chart/', views.outgoing_flow, name='outgoing_flow'),
    path('generate_incoming_flow/', views.incoming_flow, name='generate_incoming_flow'),
    path('generate_line_chart/', views.generate_line_chart, name='generate_line_chart'),
    path('generate_pie_chart_insights/', views.generate_pie_chart_insights, name='generate_pie_chart_insights'), 
    path('calculate_mean_values/', views.calculate_mean_values, name='calculate_mean_values'),
    path('generate_insights_report/', views.generate_insights_report, name='generate_insights_report'),  
    path('api/check-auth/', api_views.check_authentication, name='check_authentication'), 
    # path('api/console/', views.console_login, name='console_login'),

]
