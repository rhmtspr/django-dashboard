from django.urls import path
from dashboards.views import(
    dashboard,
    dynamic_template_dashboards_view,
    
)

app_name ='dashboards'


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('<str:template_name>/', dynamic_template_dashboards_view, name='dynamic_template_dashboards')
]
