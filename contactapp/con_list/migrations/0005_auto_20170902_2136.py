# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('con_list', '0004_contact_is_fav'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='is_fav',
            new_name='is_favorite',
        ),
    ]
