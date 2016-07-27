# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-27 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo6', '0002_auto_20160708_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosgenerales',
            name='becado_lugar',
            field=models.CharField(blank=True, choices=[('federal', 'Gobierno Federal'), ('estatal', 'Gobierno Estatal'), ('bachillerato', 'Esfuerzo de Bachillerato')], default='federal', max_length=50),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='con_quien_vives',
            field=models.CharField(choices=[('familia', 'Familia'), ('familia_cercana', 'Familia Cercana'), ('estudiantes', 'Estudiantes'), ('solo', 'Solo')], default='familia', max_length=50),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='escolaridad_madre',
            field=models.CharField(choices=[('primaria', 'Primaria'), ('secundaria', 'Secundaria'), ('preparatoria', 'Preparatoria'), ('tecnico', 'T\xe9cnico'), ('lic', 'Licenciatura'), ('posgrado ', 'Posgrado'), ('sinestudio', 'Sin estudio')], default='sinestudio', max_length=50),
        ),
        migrations.AlterField(
            model_name='datosgenerales',
            name='escolaridad_padre',
            field=models.CharField(choices=[('primaria', 'Primaria'), ('secundaria', 'Secundaria'), ('preparatoria', 'Preparatoria'), ('tecnico', 'T\xe9cnico'), ('lic', 'Licenciatura'), ('posgrado ', 'Posgrado'), ('sinestudio', 'Sin estudio')], default='sinestudio', max_length=50),
        ),
    ]
