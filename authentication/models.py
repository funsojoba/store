import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db.models.signals import post_save



class UserManager(BaseUserManager):
    user_in_migration = True

    def _create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError('email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extrafields):
        extrafields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, **extrafields)

    def create_superuser(self, email, password=None, **extrafields):
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)
        extrafields.setdefault('is_staff', True)
        return self._create_user(email=email, password=password, **extrafields)


class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

