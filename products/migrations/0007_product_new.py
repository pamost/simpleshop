# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20171208_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
