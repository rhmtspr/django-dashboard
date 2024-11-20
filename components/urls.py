from django.urls import path
from components.views import(
    dynamic_template_components_ui_view,
    dynamic_template_components_plugins_view,
    dynamic_template_components_navigation_view,
    dynamic_template_components_forms_view,
    dynamic_template_components_tables_view,
    dynamic_template_components_charts_view,
    dynamic_template_components_icons_view,
    dynamic_template_components_maps_view
)

app_name ='components'


urlpatterns = [
    path('ui/<str:template_name>/', dynamic_template_components_ui_view, name='dynamic_template_components_ui'),
    path('plugins/<str:template_name>/', dynamic_template_components_plugins_view, name='dynamic_template_components_plugins'),
    path('navigation/<str:template_name>/', dynamic_template_components_navigation_view, name='dynamic_template_components_navigation'),
    path('forms/<str:template_name>/', dynamic_template_components_forms_view, name='dynamic_template_components_forms'),
    path('tables/<str:template_name>/', dynamic_template_components_tables_view, name='dynamic_template_components_tables'),
    path('charts/<str:template_name>/', dynamic_template_components_charts_view, name='dynamic_template_components_charts'),
    path('icons/<str:template_name>/', dynamic_template_components_icons_view, name='dynamic_template_components_icons'),
    path('maps/<str:template_name>/', dynamic_template_components_maps_view, name='dynamic_template_components_maps'),
]