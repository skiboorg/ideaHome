# Generated by Django 3.0.3 on 2020-03-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_auto_20200323_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/catalog/categories/', verbose_name='Изображение категории'),
        ),
    ]
