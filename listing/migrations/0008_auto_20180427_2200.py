# Generated by Django 2.0.4 on 2018-04-27 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0007_auto_20180427_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='parkingPrice',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
