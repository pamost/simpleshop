# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='longtitle',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
