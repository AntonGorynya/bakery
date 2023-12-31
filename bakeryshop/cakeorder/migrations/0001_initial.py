# Generated by Django 4.2 on 2023-07-30 08:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=200, verbose_name='Ссылка на рекламу')),
                ('bitlink', models.CharField(blank=True, max_length=100, verbose_name='Сокращенная ссылка')),
                ('clicks', models.IntegerField(null=True, verbose_name='Количество переходов по ссылке')),
            ],
            options={
                'verbose_name': 'рекламная ссылка',
                'verbose_name_plural': 'рекламные ссылки',
            },
        ),
        migrations.CreateModel(
            name='Berries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Ягода',
                'verbose_name_plural': 'Ягоды',
            },
        ),
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Торт', max_length=50, verbose_name='Название')),
                ('occasion', models.CharField(blank=True, choices=[('T', 'На чаепитие'), ('B', 'На день рождения'), ('W', 'На свадьбу')], max_length=30, verbose_name='Повод')),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='', verbose_name='картинка')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Цена')),
                ('sign', models.CharField(blank=True, max_length=50, null=True, verbose_name='Надпись')),
                ('type', models.CharField(blank=True, choices=[('CG', 'Из каталога'), ('CM', 'Созданый пользователем')], default='CM', max_length=30, verbose_name='Тип торта')),
                ('berries', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakeorder.berries', verbose_name='Ягоды')),
            ],
            options={
                'verbose_name': 'торт',
                'verbose_name_plural': 'торты',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя клиента')),
                ('address', models.CharField(blank=True, max_length=100)),
                ('phonenumber', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('mail', models.CharField(blank=True, max_length=50, verbose_name='Электронная почта')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='клиент')),
            ],
            options={
                'verbose_name': 'клиент',
                'verbose_name_plural': 'клиенты',
            },
        ),
        migrations.CreateModel(
            name='Decor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Декор',
                'verbose_name_plural': 'Декоры',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
        migrations.CreateModel(
            name='Levels_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(unique=True, verbose_name='Количество уровней')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Количество уровней',
                'verbose_name_plural': 'Количество уровней',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Наименование')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Топпинг',
                'verbose_name_plural': 'Топпинги',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='Заказ создан')),
                ('delivery_time', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Время доставки')),
                ('comment', models.TextField(blank=True, max_length=400, verbose_name='Комментарий к заказу')),
                ('delivery_comment', models.TextField(blank=True, max_length=400, verbose_name='Комментарий курьеру')),
                ('status', models.CharField(blank=True, choices=[('Готовится', 'Готовится'), ('Доставляется', 'Доставляется'), ('Доставлен', 'Доставлен')], default='Готовится', max_length=400, verbose_name='Статус заказа')),
                ('cake', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cakeorder.cake', verbose_name='Торт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cakeorder.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
        migrations.AddField(
            model_name='cake',
            name='decor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakeorder.decor', verbose_name='Декор'),
        ),
        migrations.AddField(
            model_name='cake',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakeorder.form', verbose_name='Форма'),
        ),
        migrations.AddField(
            model_name='cake',
            name='levels_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakeorder.levels_number', verbose_name='Количество уровней'),
        ),
        migrations.AddField(
            model_name='cake',
            name='topping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cakes', to='cakeorder.topping', verbose_name='Топпинг'),
        ),
    ]
