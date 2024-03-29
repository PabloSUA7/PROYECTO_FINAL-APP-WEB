# Generated by Django 5.0.1 on 2024-02-06 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calzados', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hombres',
            old_name='color_calzado',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='descripcion_calzado',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='fecha_lanzamiento',
            new_name='fecha_Exposicion',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='material_calzado',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='nombre_calzado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='precio_calzado',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='hombres',
            old_name='talle_calzado',
            new_name='talle',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='color_calzado',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='descripcion_calzado',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='fecha_lanzamiento',
            new_name='fecha_Exposicion',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='material_calzado',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='nombre_calzado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='precio_calzado',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='mujeres',
            old_name='talle_calzado',
            new_name='talle',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='color_calzado',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='descripcion_calzado',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='fecha_lanzamiento',
            new_name='fecha_Exposicion',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='material_calzado',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='nombre_calzado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='precio_calzado',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='nenas',
            old_name='talle_calzado',
            new_name='talle',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='color_calzado',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='descripcion_calzado',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='fecha_lanzamiento',
            new_name='fecha_Exposicion',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='material_calzado',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='nombre_calzado',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='precio_calzado',
            new_name='precio',
        ),
        migrations.RenameField(
            model_name='nenes',
            old_name='talle_calzado',
            new_name='talle',
        ),
        migrations.RemoveField(
            model_name='hombres',
            name='disponible_en_stock',
        ),
        migrations.RemoveField(
            model_name='mujeres',
            name='disponible_en_stock',
        ),
        migrations.RemoveField(
            model_name='nenas',
            name='disponible_en_stock',
        ),
        migrations.RemoveField(
            model_name='nenes',
            name='disponible_en_stock',
        ),
    ]
