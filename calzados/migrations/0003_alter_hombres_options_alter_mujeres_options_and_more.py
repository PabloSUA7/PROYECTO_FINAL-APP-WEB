# Generated by Django 5.0.1 on 2024-02-28 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calzados', '0002_rename_color_calzado_hombres_color_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hombres',
            options={'verbose_name': 'un Nombre de Hombres', 'verbose_name_plural': 'Hombres'},
        ),
        migrations.AlterModelOptions(
            name='mujeres',
            options={'verbose_name': 'un Nombre de Mujeres', 'verbose_name_plural': 'Mujeres'},
        ),
        migrations.AlterModelOptions(
            name='nenas',
            options={'verbose_name': 'un Nombre de Nenas', 'verbose_name_plural': 'Nenas'},
        ),
        migrations.AlterModelOptions(
            name='nenes',
            options={'verbose_name': 'un Nombre de Nenes', 'verbose_name_plural': 'Nenes'},
        ),
    ]
