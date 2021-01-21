from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.users import forms


class SignUp(CreateView):
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy('recipes:index')
    template_name = 'signup.html'
