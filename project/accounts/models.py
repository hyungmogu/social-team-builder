from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have a valid email address")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password
        )

        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user


class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name  = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{}".format(self.email)

    def get_short_name(self):
        return self.display_name
