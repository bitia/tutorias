# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anexo13', '0002_auto_20160229_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testasertividad',
            name='pregunta1',
            field=models.CharField(max_length=50, choices=[('1', 'Con Frecuencia'), ('2', 'De vez en cuando'), ('3', 'Casi nunca'), ('4', 'Nunca')], verbose_name='En una reunión dficil, con con un ambiente tenso,soy capaz de hablar con confianza'),
        ),
    ]
