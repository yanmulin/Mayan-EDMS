# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-22 05:34
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0036_auto_20161222_0534'),
        ('checkouts', '0005_auto_20160122_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVersionBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documents.Document', verbose_name='Document')),
            ],
            options={
                'verbose_name': 'New version block',
                'verbose_name_plural': 'New version blocks',
            },
        ),
    ]
