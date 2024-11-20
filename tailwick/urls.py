
from django.contrib import admin
from django.urls import path,include
from .views import MyPasswordChangeView, MyPasswordSetView
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),


    # Dashboards
    path('', include('dashboards.urls')),

    # apps
    path('apps/', include('apps.urls')),

    # Landing
    path('landing/', include('landing.urls')),

    # Pages
    path('pages/', include('pages.urls')),

    # Pages
    path('components/', include('components.urls')),

    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),

    # all auth
    path('account/', include('allauth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
