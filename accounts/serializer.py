from accounts.models import User
from rest_framework_simplejwt.serializers import \
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD
