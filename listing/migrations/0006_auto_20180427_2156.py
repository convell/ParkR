# Generated by Django 2.0.4 on 2018-04-27 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0005_auto_20180427_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='parkingPrice',
            field=models.IntegerField(max_length=2),
        ),
    ]
