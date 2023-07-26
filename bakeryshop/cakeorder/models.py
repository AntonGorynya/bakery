from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Cake(models.Model):
    
    class OccationChoice(models.TextChoices):
        TEA = 'T', _('На чаепитие')
        BIRTHDAY = 'B', _('На день рождения')
        WEDDING = 'W', _('На свадьбу')
    
    class LevelChoice(models.TextChoices):
        ONE = 'O', _('1')
        TWO = 'TW', _('2')
        THREE = 'TH', _('3')
    
    class FormChoice(models.TextChoices):
        ROUND = 'RD', _('Круг')
        SQUARE = 'S', _('Квадрат')
        RECTANGLE = 'RL', _('Прямоугольник')
    
    class ToppingChoice(models.TextChoices):
        NO = 'N', _('Без')
        WHITE = 'W', _('Белый соус')
        CARAMEL = 'C', _('Карамель')
        MAPlE = 'M', _('Кленовый')
        BLUEBERRY = 'B', _('Черничный')
        CHOCOLATE = 'CH', _('Молочный шоколад')
        STRAWBERRY = 'S', _('Клубничный')
    
    class BerriesChoice(models.TextChoices):
        BLACKBERRY = 'BK', _('Ежевика')
        RASPBERRY = 'R', _('Малина')
        BLUEBERRY = 'BE', _('Голубика')
        STRAWBERRY = 'S', _('Клубника')
    
    class DecorChoice(models.TextChoices):
        PISTACHIOS = 'PS', _('Фисташки')
        MERINGUE = 'MR', _('Безе')
        HAZELNUT = 'H', _('Дундук')
        PECAN = 'PN', ('Пекан')
        MARSHMALLOW = 'MM', _('Макшмеллоу')
        MARZIPAN = 'MN', _('Марципан')
    
    name = models.CharField(
        'Название',
        max_length=50,
        blank=True
    )
    ocation = models.CharField(
        verbose_name='Повод',
        choices=OccationChoice.choices,
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
        choices=LevelChoice.choices,
        max_length=30,
        blank=True
    )
    form = models.CharField(
        verbose_name='Форма',
        choices=FormChoice.choices,
        max_length=30,
        blank=True
    )
    topping = models.CharField(
        verbose_name='Топпинг',
        choices=ToppingChoice.choices,
        max_length=30,
        blank=True
    )
    berries = models.CharField(
        verbose_name='Ягоды',
        choices=BerriesChoice.choices,
        max_length=30,
        blank=True
    )
    decor = models.CharField(
        verbose_name='Декор',
        choices=DecorChoice.choices,
        max_length=30,
        blank=True
    )
    sign = models.CharField(
        'Надпись',
        max_length=50,
        blank=True
    )
    
    def __str__(self):
        return f"{self.name} {self.ocation}"


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
    
    def __str__(self):
        return f"{self.name}: {self.address}, {self.phonenumber}"


class Order(models.Model):
    cake = models.ForeignKey(
        Cake,
        verbose_name='Название торта',
        on_delete=models.CASCADE,
        related_name='orders'
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
