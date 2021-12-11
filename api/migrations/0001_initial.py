# Generated by Django 3.2 on 2021-12-11 14:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=200, verbose_name='ИНН')),
                ('OGRN', models.CharField(max_length=200, verbose_name='ОГРН')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('occupation', models.CharField(max_length=400, verbose_name='Деятельность')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('address', models.CharField(max_length=400, verbose_name='Адрес')),
                ('registration_date', models.DateField(verbose_name='Дата основания')),
                ('website', models.CharField(max_length=200, verbose_name='Вебсайт')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('rating', models.CharField(blank=True, choices=[('AAA', 'Aaa'), ('AA', 'Aa'), ('A', 'A'), ('BBB', 'Bbb'), ('BB', 'Bb'), ('B', 'B'), ('CCC', 'Ccc'), ('CC', 'Cc'), ('C', 'C')], max_length=4, null=True, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'db_table': 'companies',
                'ordering': ['inn'],
            },
        ),
        migrations.CreateModel(
            name='CompanyAccounting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год')),
                ('month', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Месяц')),
                ('revenue', models.FloatField(verbose_name='Выручка')),
                ('operating_profit', models.FloatField(verbose_name='Операционная прибыль')),
                ('net_profit', models.FloatField(verbose_name='Чистая прибыль')),
                ('debt', models.FloatField(verbose_name='Долг')),
            ],
            options={
                'verbose_name': 'Данные компании',
                'db_table': 'accounting',
                'ordering': ['year', 'month'],
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата выплаты')),
            ],
            options={
                'verbose_name': 'Купон',
                'verbose_name_plural': 'Купоны',
                'db_table': 'coupons',
                'ordering': ['request', 'date'],
            },
        ),
        migrations.CreateModel(
            name='James',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата совершения')),
                ('sum', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Сумма инвестирования')),
            ],
            options={
                'verbose_name': 'Джеймс',
                'verbose_name_plural': 'Джеймсы',
                'db_table': 'james',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Сумма')),
                ('post_date', models.DateField(auto_now_add=True, verbose_name='Дата выставления')),
                ('expiration_date', models.DateField(verbose_name='Дата завершения')),
                ('buy_date', models.DateField(blank=True, null=True, verbose_name='Дата совершения сделки')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
                'db_table': 'lots',
                'ordering': ['post_date'],
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Ставка')),
                ('goal', models.CharField(max_length=200, verbose_name='Цель')),
                ('soft_cap', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Мин. сумма')),
                ('soft_end_date', models.DateField(verbose_name='Дата окончания сбора мин. суммы')),
                ('hard_cap', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Макс. сумма')),
                ('hard_end_date', models.DateField(verbose_name='Дата окончания сбора макс. суммы')),
                ('min_payment', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Мин. взнос')),
            ],
            options={
                'verbose_name': 'Запрос',
                'verbose_name_plural': 'Запросы',
                'db_table': 'requests',
                'ordering': ['company'],
            },
        ),
        migrations.CreateModel(
            name='RequestCashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(verbose_name='Величина')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Денежный поток запроса',
                'db_table': 'request_cash_flow',
                'ordering': ['request', 'date'],
            },
        ),
        migrations.CreateModel(
            name='RequestCashTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип транзакции запроса',
                'verbose_name_plural': 'Типы транзакций запроса',
                'db_table': 'request_cash_transaction_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserCashTransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип транзакции пользователя',
                'verbose_name_plural': 'Типы транзакций пользователя',
                'db_table': 'user_cash_transaction_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserCashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.FloatField(verbose_name='Величина')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('tx_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.usercashtransactiontype', verbose_name='Тип транзакции')),
            ],
            options={
                'verbose_name': 'Денежный поток пользователя',
                'db_table': 'user_cash_flow',
                'ordering': ['user', 'date'],
            },
        ),
    ]
