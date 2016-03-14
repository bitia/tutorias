# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('anexo13', '0005_auto_20160308_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testasertividad',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
