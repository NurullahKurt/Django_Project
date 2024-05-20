from .views import RegistrationView, UsernameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('validate-username', csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    # path('validate-username', UsernameValidationView.as_view(), name="validate-username"),
]