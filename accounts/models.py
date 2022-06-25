from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager ## A new class is imported. ##

ADMIN = 1
VENDOR = 2
CUSTOMER = 3

USER_TYPE_CHOICES = (
    (ADMIN, 'ADMIN'),
    (VENDOR, 'VENDOR'),
    (CUSTOMER, 'CUSTOMER'),
)


class User(AbstractUser):
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.png', upload_to='images/profile/')
    bio = models.TextField()
    dob = models.DateField()
    address = models.TextField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
