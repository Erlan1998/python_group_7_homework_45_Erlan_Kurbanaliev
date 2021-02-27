# Generated by Django 3.1.7 on 2021-02-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20210225_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='detailed_description',
            field=models.TextField(default='detailed_description', max_length=3000),
        ),
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
