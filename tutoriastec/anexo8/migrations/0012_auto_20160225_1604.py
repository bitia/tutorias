# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo8', '0011_areapsicopedagogica_plandevida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areapsicopedagogica',
            name='rendimiento_escolar',
            field=models.CharField(choices=[('1', 'Muy bueno'), ('2', 'Bueno'), ('3', 'Regular'), ('4', 'Malo'), ('5', 'Muy malo')], default='2', max_length=50),
        ),
    ]