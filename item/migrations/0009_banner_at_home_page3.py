# Generated by Django 3.1.4 on 2021-02-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_auto_20210202_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='at_home_page3',
            field=models.BooleanField(default=False, verbose_name='На главной (баннер3)'),
        ),
    ]
