# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateTimeField()),
                ('idade', models.IntegerField()),
                ('ativo', models.BooleanField()),
            ],
        ),
    ]