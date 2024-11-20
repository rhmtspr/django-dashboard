from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

@login_required
def dynamic_template_apps_view(request, template_name):
    try:
        return render(request, f'apps/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')

@login_required    
def dynamic_template_apps_calendar_view(request, template_name):
    try:
        return render(request, f'apps/calendar/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')    

@login_required    
def dynamic_template_apps_ecommerce_view(request, template_name):
    try:
        return render(request, f'apps/ecommerce/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')      

@login_required    
def dynamic_template_apps_hr_view(request, template_name):
    try:
        return render(request, f'apps/hr/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')    

@login_required
def dynamic_template_apps_social_view(request, template_name):
    try:
        return render(request, f'apps/social/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')          

@login_required    
def dynamic_template_apps_invoice_view(request, template_name):
    try:
        return render(request, f'apps/invoice/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')    

@login_required
def dynamic_template_apps_users_view(request, template_name):
    try:
        return render(request, f'apps/users/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')              