# Generated by Django 4.1 on 2022-09-01 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudrh', '0005_remove_empleados_cedula_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidatos',
            name='principales_capacitaciones',
        ),
        migrations.RemoveField(
            model_name='candidatos',
            name='principales_competencias',
        ),
        migrations.AddField(
            model_name='candidatos',
            name='principales_capacitaciones',
            field=models.ManyToManyField(to='crudrh.capacitaciones'),
        ),
        migrations.AddField(
            model_name='candidatos',
            name='principales_competencias',
            field=models.ManyToManyField(to='crudrh.competencias'),
        ),
    ]
