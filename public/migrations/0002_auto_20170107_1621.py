# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='socio_professional_category',
            new_name='social_professional_category',
        ),
    ]
