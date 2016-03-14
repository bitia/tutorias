# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anexo8', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='dificultades_dormir',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='dolores_cabeza',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='fatiga',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='incontinecia',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='perdida_vista',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='perdidad_equilibrio',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='pesadillas',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AddField(
            model_name='estadopsicofisiologicos',
            name='tartamudeo',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
        migrations.AlterField(
            model_name='estadopsicofisiologicos',
            name='dolores_vientre',
            field=models.CharField(choices=[('1', 'Muy frecuente'), ('2', 'Frecuente'), ('3', 'A veces'), ('4', 'Antes'), ('5', 'Nunca')], default='5', max_length=50),
        ),
    ]