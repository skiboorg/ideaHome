# Generated by Django 3.0.3 on 2020-03-11 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
        ('customuser', '0001_initial'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Корзина клиента'),
        ),
        migrations.AddField(
            model_name='cart',
            name='guest',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='customuser.Guest', verbose_name='Корзина гостя'),
        ),
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='Товар'),
        ),
    ]
