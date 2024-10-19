from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Registration(models.Model):
    name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CreateUserLoginManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class CreateUserLogin(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CreateUserLoginManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin