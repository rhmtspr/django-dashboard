from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.template import TemplateDoesNotExist

@login_required
def dynamic_template_dashboards_view(request, template_name):
    try:
        return render(request, f'dashboards/{template_name}.html')
    except TemplateDoesNotExist:
        return render(request, f'pages/pages/pages-404.html')
    
@login_required    
def dashboard(request):
    return render(request, 'dashboards/index.html')    