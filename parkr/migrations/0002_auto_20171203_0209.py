# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspace',
            name='owner',
            field=models.TextField(),
        ),
    ]
