# Generated by Django 4.1 on 2023-07-26 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeorder', '0002_remove_cake_ocation_cake_occasion_cake_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cake',
            options={'verbose_name': 'торт', 'verbose_name_plural': 'торты'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterField(
            model_name='order',
            name='cake',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cakeorder.cake', verbose_name='Торт'),
        ),
    ]
