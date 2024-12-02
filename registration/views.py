from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirige al login después de registrarse

    def form_valid(self, form):
        response = super().form_valid(form)
        # Aquí puedes agregar lógica adicional si lo necesitas (como enviar un correo de bienvenida)
        return response
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Personaliza tu plantilla si es necesario
    success_url = reverse_lazy('home')  # O la página a la que quieras redirigir después de iniciar sesión

    def form_valid(self, form):
        return super().form_valid(form)
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
