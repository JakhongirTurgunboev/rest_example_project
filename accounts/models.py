from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        # Ensure that only superusers can be created using this method
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    REQUIRED_FIELDS = []
    objects = UserManager()
