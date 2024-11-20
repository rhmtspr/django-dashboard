from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

@login_required
def dynamic_template_components_ui_view(request, template_name):
    try:
        return render(request, f'components/ui/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')
    
@login_required    
def dynamic_template_components_plugins_view(request, template_name):
    try:
        return render(request, f'components/plugins/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')    

@login_required       
def dynamic_template_components_navigation_view(request, template_name):
    try:
        return render(request, f'components/navigation/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')     

@login_required       
def dynamic_template_components_forms_view(request, template_name):
    try:
        return render(request, f'components/forms/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')
  
@login_required   
def dynamic_template_components_tables_view(request, template_name):
    try:
        return render(request, f'components/tables/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')         

@login_required
def dynamic_template_components_charts_view(request, template_name):
    try:
        return render(request, f'components/charts/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')         

@login_required    
def dynamic_template_components_icons_view(request, template_name):
    try:
        return render(request, f'components/icons/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')  

@login_required
def dynamic_template_components_maps_view(request, template_name):
    try:
        return render(request, f'components/maps/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')          