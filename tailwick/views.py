
# from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import PasswordChangeView, PasswordSetView
from django.urls import reverse_lazy



class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("dashboard")


class MyPasswordSetView(PasswordSetView):
    success_url = reverse_lazy("dashboard")