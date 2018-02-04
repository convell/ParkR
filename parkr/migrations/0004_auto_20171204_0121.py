# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkr', '0003_auto_20171203_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkingspace',
            name='timeClose',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='timeOpen',
            field=models.CharField(default=b'0', max_length=b'300'),
        ),
    ]
