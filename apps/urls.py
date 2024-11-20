from django.urls import path
from apps.views import(
    dynamic_template_apps_view,
    dynamic_template_apps_calendar_view,
    dynamic_template_apps_ecommerce_view,
    dynamic_template_apps_hr_view,
    dynamic_template_apps_social_view,
    dynamic_template_apps_invoice_view,
    dynamic_template_apps_users_view
)

app_name ='apps'


urlpatterns = [
    path('<str:template_name>/', dynamic_template_apps_view, name='dynamic_template_apps'),
    path('calendar/<str:template_name>/', dynamic_template_apps_calendar_view, name='dynamic_template_apps_calendar'),
    path('ecommerce/<str:template_name>/', dynamic_template_apps_ecommerce_view, name='dynamic_template_apps_ecommerce'),
    path('hr/<str:template_name>/', dynamic_template_apps_hr_view, name='dynamic_template_apps_hr'),
    path('social/<str:template_name>/', dynamic_template_apps_social_view, name='dynamic_template_apps_social'),
    path('invoice/<str:template_name>/', dynamic_template_apps_invoice_view, name='dynamic_template_apps_invoice'),
    path('users/<str:template_name>/', dynamic_template_apps_users_view, name='dynamic_template_apps_users'),
]