from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Отправка письма
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию на нашем сайте.',
            'test.test.Django@yandex.com',
            [self.object.email],
            fail_silently=False,
        )

        return response


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = EmailAuthenticationForm