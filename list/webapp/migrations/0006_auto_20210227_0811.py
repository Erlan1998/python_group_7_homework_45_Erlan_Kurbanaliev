# Generated by Django 3.1.7 on 2021-02-27 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210227_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=3000, null=True),
        ),
    ]
