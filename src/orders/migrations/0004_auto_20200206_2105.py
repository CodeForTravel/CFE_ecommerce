# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-02-06 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200205_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='billing_profie',
            new_name='billing_profile',
        ),
    ]
