from django.contrib.auth.backends import ModelBackend
from .models import CreateUserLogin
from django.contrib.auth.hashers import check_password

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CreateUserLogin.objects.get(username=username)
            if user and check_password(password, user.password):
                return user
        except CreateUserLogin.DoesNotExist:
            return None
