# Generated by Django 3.1.7 on 2021-03-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210227_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
