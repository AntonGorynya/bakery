from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Levels_number(models.Model):
    quantity = models.IntegerField(
        verbose_name='Количество уровней',
        unique =True,
        )
    class Meta:
        verbose_name = 'Количество уровней'
        verbose_name_plural = 'Количество уровней'

    def __str__(self):
        return str(self.quantity)

class Form (models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=30,
        unique =True,
        )
    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return self.name

class Topping (models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=30,
        unique =True,
        )
    availability = models.BooleanField(
        verbose_name='Наличие',
        default=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self):
        return self.name

class Berries (models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=30,
        unique =True,
        )
    availability = models.BooleanField(
        verbose_name='Наличие',
        default=True)

    class Meta:
        verbose_name = 'Ягода'
        verbose_name_plural = 'Ягоды'

    def __str__(self):
        return self.name


class Decor (models.Model):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=30,
        unique =True,
        )
    availability = models.BooleanField(
        verbose_name='Наличие',
        default=True)

    class Meta:
        verbose_name = 'Декор'
        verbose_name_plural = 'Декоры'

    def __str__(self):
        return self.name


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
    levels_number = models.ForeignKey(
        Levels_number,
        verbose_name='Количество уровней',
        on_delete=models.PROTECT,
        related_name='cakes',
        blank=True
    )
    form = models.ForeignKey(
        Form,
        verbose_name='Форма',
        on_delete=models.PROTECT,
        related_name='cakes',
        blank=True
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name='Топпинг',
        on_delete=models.PROTECT,
        related_name='cakes',
        blank=True
    )
    berries = models.ForeignKey(
        Berries,
        verbose_name='Ягоды',
        on_delete=models.PROTECT,
        related_name='cakes',
        blank=True
    )
    decor = models.ForeignKey(
        Decor,
        verbose_name='Декор',
        on_delete=models.PROTECT,
        related_name='cakes',
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



