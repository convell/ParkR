# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkr', '0002_auto_20171203_0209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkingspace',
            name='location',
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='lat',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='lng',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
        migrations.AlterField(
            model_name='parkingspace',
            name='note',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
        migrations.AlterField(
            model_name='parkingspace',
            name='owner',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
    ]
