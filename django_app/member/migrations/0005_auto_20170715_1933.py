# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20170715_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('D', 'Django'), ('F', 'Facebook'), ('G', 'Google'), ('N', 'Naver')], default='D', max_length=1),
        ),
    ]
