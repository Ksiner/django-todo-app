from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is Required")

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")

        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email, password, **kwargs)


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, null=False)
    name = models.CharField(
        max_length=200,
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return self.name
