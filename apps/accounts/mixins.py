from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMixin(AccessMixin):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class LogoutRequiredMixin:
    @method_decorator(login_required(login_url='signin'))
    def dispatch(self, request, *args, **kwargs):
        # Store the current page URL in the session for redirection after logout
        request.session['next_page'] = request.get_full_path()
        return super().dispatch(request, *args, **kwargs)