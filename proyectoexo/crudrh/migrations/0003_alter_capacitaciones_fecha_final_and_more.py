# Generated by Django 4.1 on 2022-09-01 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudrh', '0002_alter_candidatos_principales_capacitaciones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitaciones',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='capacitaciones',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experiencia_laboral',
            name='fecha_final',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experiencia_laboral',
            name='fecha_inicio',
            field=models.DateField(null=True),
        ),
    ]
