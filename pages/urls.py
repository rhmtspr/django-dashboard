from django.urls import path
from pages.views import(
    dynamic_template_pages_auth_view,
    dynamic_template_pages_pages_view
)

app_name ='pages'


urlpatterns = [
    path('auth/<str:template_name>/', dynamic_template_pages_auth_view, name='dynamic_template_pages_auth'),
    path('pages/<str:template_name>/', dynamic_template_pages_pages_view, name='dynamic_template_pages_pages'),
]