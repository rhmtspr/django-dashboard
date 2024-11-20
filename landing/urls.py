from django.urls import path
from landing.views import(
    dynamic_template_landing_view,
    
)

app_name ='landing'


urlpatterns = [
    path('<str:template_name>/', dynamic_template_landing_view, name='dynamic_template_landing')
]