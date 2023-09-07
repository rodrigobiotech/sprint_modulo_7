# Generated by Django 4.1.7 on 2023-09-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Completada', 'Completada'), ('Cancelada', 'Cancelada')], max_length=30),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='etiqueta',
            field=models.CharField(choices=[('Trabajo', 'Trabajo'), ('Hogar', 'Hogar'), ('Estudio', 'Estudio')], max_length=30),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='prioridad',
            field=models.CharField(choices=[('Baja', 'Baja'), ('Media', 'Media'), ('Alta', 'Alta'), ('Crítica', 'Crítica')], max_length=40),
        ),
    ]