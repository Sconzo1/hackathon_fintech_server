from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from authentication.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    phone = PhoneNumberField(unique=True, help_text='Номер телефона')
    password = models.CharField('Пароль', max_length=300)

    email = models.EmailField('Email', max_length=100)
    full_name = models.CharField('ФИО', max_length=150)
    birthdate = models.DateField('Дата рождения', null=True, blank=True)
    passport_serial = models.CharField('Серия паспорта', null=True, max_length=4)
    passport_num = models.CharField('Номер паспорта', null=True, max_length=6)
    is_verified = models.BooleanField('Верифицирован?', default=False)

    is_staff = models.BooleanField('Модератор?', default=False)
    is_superuser = models.BooleanField('Суперпользователь?', default=False)
    last_login = models.DateTimeField('Время последнего входа', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['phone']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.full_name}"
