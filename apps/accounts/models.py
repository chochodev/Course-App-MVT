import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.accounts.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  first_name = models.CharField(verbose_name=(_("First name")), max_length=25, null=True)
  last_name = models.CharField(verbose_name=(_("Last name")), max_length=25, null=True)
  username = models.CharField(verbose_name=(_("Username")), unique=True, max_length=25, null=True)
  email = models.EmailField(verbose_name=(_("Email address")), unique=True)

  is_email_verified = models.BooleanField(default=True)
  is_logged_in = models.BooleanField(default=True)
  date_joined = models.DateTimeField(default=timezone.now)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = ["first_name", "last_name", "username"]

  objects = CustomUserManager()

  class Meta:
    verbose_name = _("User")
    verbose_name_plural = _("Users")

  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  def __str__(self):
    return self.full_name
