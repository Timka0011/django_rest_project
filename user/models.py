from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager

# Create your models here.

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class User(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=150)
    phone = models.CharField(
                             max_length=12,
                             unique=True,
                             help_text='Required. 12 characters or fewer. Digits only.',
                             # validators=[phone_regex],
                             error_messages={
                                 'unique': "Bu telefon raqamga ega foydalanuvchi oldindan mavjud",
                             },
                             )
    location = models.CharField(max_length=200, null=True, blank=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.phone
