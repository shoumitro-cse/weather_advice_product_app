from django.db import models
from django.contrib.auth.models import AbstractUser ## A new class is imported. ##
from accounts.manager import UserManager
from base.constants import CUSTOMER, ADMIN, VENDOR


class User(AbstractUser):

    USER_TYPE_CHOICES = (
        (ADMIN, 'ADMIN'),
        (VENDOR, 'VENDOR'),
        (CUSTOMER, 'CUSTOMER'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    email = models.EmailField("email address", blank=True, unique=True)

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(default='default.png', upload_to='images/profile/')
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.email
