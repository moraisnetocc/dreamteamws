import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateField('Data de cadastro', default=datetime.date.today)
    date_of_birth = models.DateField('Data de nascimento', blank=True, null=True)
    cep = models.CharField('CEP', max_length=10, blank=True, null=True)
    street = models.CharField('Rua', max_length=100, blank=True, null=True)
    neighborhood = models.CharField('Bairro', max_length=100, blank=True, null=True)
    city = models.CharField('Cidade', max_length=100, blank=True, null=True)
    state = models.CharField('Estado', max_length=100, blank=True, null=True)
    name = models.CharField('Nome', max_length=100, blank=True, null=True)
    last_name = models.CharField('Sobrenome', max_length=100, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=15, blank=True, null=True)
    photo = models.ImageField('Foto', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
