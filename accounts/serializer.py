from accounts.models import User, Profile
from rest_framework_simplejwt.serializers import \
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer
from rest_framework import serializers

from base.constants import ADMIN


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'user_type',
            'is_active',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        if validated_data["user_type"] == ADMIN:
            user.is_superuser = True
            user.is_staff = True
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('user', )
