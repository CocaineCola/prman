# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-10 23:53
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_courseorg_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u673a\u6784\u63cf\u8ff0'),
        ),
    ]
