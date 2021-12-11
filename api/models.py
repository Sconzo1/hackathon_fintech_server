import calendar
import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError


# Reference tables

class UserCashTransactionType(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'user_cash_transaction_types'
        ordering = ['name']
        verbose_name = 'Тип транзакции пользователя'
        verbose_name_plural = 'Типы транзакций пользователя'

    def __str__(self):
        return self.name


class RequestCashTransactionType(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'request_cash_transaction_types'
        ordering = ['name']
        verbose_name = 'Тип транзакции запроса'
        verbose_name_plural = 'Типы транзакций запроса'

    def __str__(self):
        return self.name


# Operated models tables


class Company(models.Model):
    class Ratings(models.TextChoices):
        AAA = 'AAA'
        AA = 'AA'
        A = 'A'
        BBB = 'BBB'
        BB = 'BB'
        B = 'B'
        CCC = 'CCC'
        CC = 'CC'
        C = 'C'

    inn = models.CharField('ИНН', max_length=200)
    OGRN = models.CharField('ОГРН', max_length=200)
    name = models.CharField('Название', max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Представитель/Владелец")
    occupation = models.CharField('Деятельность', max_length=400)
    desc = models.TextField('Описание')
    address = models.CharField('Адрес', max_length=400)
    registration_date = models.DateField('Дата основания')
    website = models.CharField('Вебсайт', max_length=200)
    photo = models.ImageField('Фото', null=True, blank=True)
    rating = models.CharField('Рейтинг', choices=Ratings.choices, max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'companies'
        ordering = ['inn']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class CompanyAccounting(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Компания")
    year = models.PositiveSmallIntegerField('Год')
    month = models.PositiveSmallIntegerField('Месяц', validators=[MinValueValidator(1), MaxValueValidator(12)])
    revenue = models.FloatField('Выручка')
    operating_profit = models.FloatField('Операционная прибыль')
    net_profit = models.FloatField('Чистая прибыль')
    debt = models.FloatField('Долг')

    class Meta:
        db_table = 'accounting'
        ordering = ['year', 'month']
        verbose_name = 'Данные компании'
        verbose_name_plural = 'Данные компании'

    def __str__(self):
        return f"{self.year} || {calendar.month_name[self.month - 1]} ({self.month})"


class Request(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name="Компания")
    rate = models.FloatField('Ставка', validators=[MinValueValidator(0.0)])
    goal = models.CharField('Цель', max_length=200)
    soft_cap = models.FloatField('Мин. сумма', validators=[MinValueValidator(0.0)])
    soft_end_date = models.DateField('Дата окончания сбора мин. суммы')
    hard_cap = models.FloatField('Макс. сумма', validators=[MinValueValidator(0.0)])
    hard_end_date = models.DateField('Дата окончания сбора макс. суммы')
    min_payment = models.FloatField('Мин. взнос', validators=[MinValueValidator(0.0)])

    def _validate(self):
        if self.soft_cap > self.hard_cap:
            raise ValidationError("Soft cap cannot be more than hard cap")
        if self.min_payment > self.hard_cap:
            raise ValidationError("Minimum payment value cannot be more than hard cap")
        if self.soft_end_date <= datetime.date.today():
            raise ValidationError("Soft end date cannot be in the past")
        if self.hard_end_date <= datetime.date.today():
            raise ValidationError("Hard end date cannot be in the past")
        if self.soft_end_date > self.hard_end_date:
            raise ValidationError("Hard end date cannot be before soft end date")

    def save(self, *args, **kwargs):
        self._validate()
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'requests'
        ordering = ['company']
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f"{self.company} || {self.goal}"


class Coupon(models.Model):
    request = models.ForeignKey(Request, on_delete=models.PROTECT, verbose_name="Запрос")
    date = models.DateField('Дата выплаты')

    class Meta:
        db_table = 'coupons'
        ordering = ['request', 'date']
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'

    def __str__(self):
        return f"{self.request} || {self.date}"


class James(models.Model):
    request = models.ForeignKey(Request, on_delete=models.PROTECT, verbose_name="Запрос")
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Инвестор")
    date = models.DateField('Дата совершения', auto_now_add=True)
    sum = models.FloatField('Сумма инвестирования', validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'james'
        ordering = ['date']
        verbose_name = 'Джеймс'
        verbose_name_plural = 'Джеймсы'

    def __str__(self):
        return f"{self.request} || {self.user}"


class Lot(models.Model):
    request = models.ForeignKey(Request, on_delete=models.PROTECT, verbose_name="Запрос")
    seller = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='seller',
                               verbose_name="Продавец")
    buyer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, related_name='buyer',
                              verbose_name="Покупатель", null=True, blank=True)
    sum = models.FloatField('Сумма', validators=[MinValueValidator(0.0)])
    post_date = models.DateField('Дата выставления', auto_now_add=True)
    expiration_date = models.DateField('Дата завершения')
    buy_date = models.DateField('Дата совершения сделки', null=True, blank=True)

    class Meta:
        db_table = 'lots'
        ordering = ['post_date']
        verbose_name = 'Лот'
        verbose_name_plural = 'Лоты'

    def __str__(self):
        return f"{self.request} || {self.seller} -> {self.buyer} || {self.buy_date}"


class RequestCashFlow(models.Model):
    request = models.ForeignKey(Request, on_delete=models.PROTECT, verbose_name="Запрос")
    sum = models.FloatField('Величина')
    date = models.DateField('Дата', auto_now_add=True)
    tx_type = models.ForeignKey(RequestCashTransactionType, on_delete=models.PROTECT, verbose_name='Тип транзакции')

    class Meta:
        db_table = 'request_cash_flow'
        ordering = ['request', 'date']
        verbose_name = 'Денежный поток запроса'
        verbose_name_plural = 'Денежный поток запроса'

    def __str__(self):
        return f"{self.request} || {self.date} {self.sum}"


class UserCashFlow(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Инвестор")
    sum = models.FloatField('Величина')
    date = models.DateField('Дата', auto_now_add=True)
    tx_type = models.ForeignKey(UserCashTransactionType, on_delete=models.PROTECT, verbose_name='Тип транзакции')

    class Meta:
        db_table = 'user_cash_flow'
        ordering = ['user', 'date']
        verbose_name = 'Денежный поток пользователя'
        verbose_name_plural = 'Денежный поток пользователя'

    def __str__(self):
        return f"{self.user} || {self.date} {self.sum}"
