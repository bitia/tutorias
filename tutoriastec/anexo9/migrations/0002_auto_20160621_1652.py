# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-21 16:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anexo9', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineadelavida',
            name='comentario',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 6, 21, 16, 51, 40, 288740, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='etapa1',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='etapa2',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='etapa3',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='etapa4',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 6, 21, 16, 52, 8, 529987, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lineadelavida',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
