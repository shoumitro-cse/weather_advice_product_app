from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from accounts.models import User


class EmailBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            email = kwargs.get('email', None)
            if email is None:
                email = kwargs.get('username', None)
            user = User.objects.get(email=email)
            if user.check_password(kwargs.get('password', None)):
                return user
        except User.DoesNotExist:
            return None
        return None