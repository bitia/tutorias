# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-05 13:54
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anexo11', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventarioEstudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('pregunta1', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Me ayuda trazar o escribir a mano las palabras cuando tengo que aprenderlas de Memoria')),
                ('pregunta2', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Recuerdo mejor un tema al escuchar una conferencia en vez de leer un libro de Texto')),
                ('pregunta3', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero las clases que requieren una prueba sobre lo que se lee en el libro de Texto')),
                ('pregunta4', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Me gusta comer bocados y mascar chicle, cuando estudio')),
                ('pregunta5', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Al prestar atenci\xc3\xb3n a una conferencia, puedo recordar las ideas principales sin Anotarlas')),
                ('pregunta6', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero las instrucciones escritas sobre las orales')),
                ('pregunta7', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Yo resuelvo bien los rompecabezas y los laberintos')),
                ('pregunta8', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero las clases que requieran una prueba sobre lo que se presenta durante  una conferencia')),
                ('pregunta9', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Me ayuda ver diapositivas y videos para comprender un tema')),
                ('pregunta10', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Recuerdo m\xc3\xa1s cuando leo un libro que cuando escucho una conferencia')),
                ('pregunta11', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Por lo general, tengo que escribir los n\xc3\xbameros del tel\xc3\xa9fono para recordarlos bien')),
                ('pregunta12', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero recibir las noticias escuchando la radio en vez de leerlas en un peri\xc3\xb3dico')),
                ('pregunta13', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Me gusta tener algo como un bol\xc3\xadgrafo o un l\xc3\xa1piz en la mano cuando estudio')),
                ('pregunta14', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Necesito copiar los ejemplos de la pizarra del maestro para examinarlos m\xc3\xa1s Tarde')),
                ('pregunta15', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero las instrucciones orales del maestro a aquellas escritas en un examen o en la pizarra')),
                ('pregunta16', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero que un libro de texto tenga diagramas gr\xc3\xa1ficos y cuadros porque me ayudan mejor a  entender el material')),
                ('pregunta17', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Me gusta escuchar m\xc3\xbasica al estudiar una obra, novela, etc.')),
                ('pregunta18', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Tengo que apuntar listas de cosas que quiero hacer para recordarlas')),
                ('pregunta19', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Puedo corregir mi tarea examin\xc3\xa1ndola y encontrando la mayor\xc3\xada de los errores')),
                ('pregunta20', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Prefiero leer el peri\xc3\xb3dico en vez de escuchar las noticias')),
                ('pregunta21', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Puedo recordar los n\xc3\xbameros de tel\xc3\xa9fono cuando los oigo')),
                ('pregunta22', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Gozo el trabajo que me exige usar la mano o herramientas')),
                ('pregunta23', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Cuando escribo algo, necesito leerlo en voz alta para o\xc3\xadr como suena')),
                ('pregunta24', models.CharField(choices=[('1', 'Nunca'), ('2', 'Raramente'), ('3', 'Ocacionalmente'), ('4', 'Usualmente'), ('5', 'Siempre')], max_length=2, verbose_name=b'Puedo recordar mejor las cosas cuando puedo moverme mientras estoy aprendi\xc3\xa9ndolas, por ej. caminar al estudiar, o participar en una actividad que me permita moverme, etc.')),
                ('diagnostico', models.CharField(blank=True, choices=[('0', 'Visual'), ('1', 'Auditivo'), ('2', 'Kinestesico')], max_length=2)),
                ('comentarios', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('usuario', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
