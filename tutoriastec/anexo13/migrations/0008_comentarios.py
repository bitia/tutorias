# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anexo13', '0007_auto_20160310_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('tutor', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True)),
                ('tutorado', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
    ]
