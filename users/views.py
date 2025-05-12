from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
    success_url = reverse_lazy("diary:home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = reverse_lazy("users:login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
