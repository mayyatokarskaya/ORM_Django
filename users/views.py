from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm, EmailAuthenticationForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        # Отправка письма
        send_mail(
            "Добро пожаловать!",
            "Спасибо за регистрацию на нашем сайте.",
            "test.test.Django@yandex.com",
            [self.object.email],
            fail_silently=False,
        )

        return response


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = EmailAuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, f"Добро пожаловать, {form.get_user().email}!")
        return super().form_valid(form)
