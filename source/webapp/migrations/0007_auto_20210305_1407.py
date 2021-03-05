# Generated by Django 3.1.7 on 2021-03-05 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210305_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Разное'), ('sports', 'Спортивне'), ('Classic', 'Классические'), ('For home', 'Для дома'), ('for study', 'Для учебы')], default='other', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]