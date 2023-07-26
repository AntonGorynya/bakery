from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Cake(models.Model):
    
    class OccasionChoice(models.TextChoices):
        TEA = 'T', _('На чаепитие')
        BIRTHDAY = 'B', _('На день рождения')
        WEDDING = 'W', _('На свадьбу')
    
    class TypeChoice(models.TextChoices):
        CATALOG = 'CG', _('Из каталога')
        CUSTOM = 'CM', _('Созданый пользователем')
    

    name = models.CharField(
        'Название',
        max_length=50,
        blank=True
    )
    occasion = models.CharField(
        verbose_name='Повод',
        choices=OccasionChoice.choices,
        max_length=30,
        blank=True
    )
    image = models.ImageField(
        'картинка',
        blank=True
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name='Цена',
        blank=True
    )
    levels_number = models.CharField(
        verbose_name='Количество уровней',
        max_length=30,
        blank=True
    )
    form = models.CharField(
        verbose_name='Форма',
        max_length=30,
        blank=True
    )
    topping = models.CharField(
        verbose_name='Топпинг',
        max_length=30,
        blank=True
    )
    berries = models.CharField(
        verbose_name='Ягоды',
        max_length=30,
        blank=True
    )
    decor = models.CharField(
        verbose_name='Декор',
        max_length=30,
        blank=True
    )
    sign = models.CharField(
        'Надпись',
        max_length=50,
        blank=True
    )
    type = models.CharField(
        verbose_name='Тип торта',
        choices=TypeChoice.choices,
        max_length=30,
        blank=True
    )
    
    class Meta:
        verbose_name = 'торт'
        verbose_name_plural = 'торты'
    
    def __str__(self):
        return f"{self.name} {self.occasion}"

class Customer(models.Model):
    name = models.CharField(
        'ФИО клиента',
        max_length=50,
    )
    address = models.CharField(
        max_length=100,
        blank=True,
    )
    phonenumber = models.CharField(
        'Номер телефона',
        max_length=50
    )
    mail = models.CharField(
        'Электронная почта',
        max_length=50,
        blank=True
    )
    
    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
    
    def __str__(self):
        return f"{self.name}: {self.address}, {self.phonenumber}"


class Order(models.Model):
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True
    )
    customer = models.ForeignKey(
        Customer,
        verbose_name='Клиент',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    created_time = models.DateTimeField(
        'Заказ создан',
        default=timezone.now,
        db_index=True
    )
    delivery_time = models.DateTimeField(
        'Время доставки',
        null=True,
        blank=True,
        db_index=True
    )
    comment = models.TextField(
        verbose_name='Комментарий к заказу',
        blank=True,
        max_length=400
    )
    delivery_comment = models.TextField(
        verbose_name='Комментарий курьеру',
        blank=True,
        max_length=400
    )
    
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
    
    def __str__(self):
        return f"{self.customer.name}: {self.customer.phonenumber}"
