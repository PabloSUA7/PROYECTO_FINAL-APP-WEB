# Generated by Django 5.0.1 on 2024-02-05 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hombres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calzado', models.CharField(max_length=50)),
                ('descripcion_calzado', models.CharField(max_length=50)),
                ('talle_calzado', models.IntegerField()),
                ('precio_calzado', models.CharField(max_length=50)),
                ('color_calzado', models.CharField(max_length=20)),
                ('material_calzado', models.CharField(max_length=50)),
                ('disponible_en_stock', models.BooleanField(default=True)),
                ('fecha_lanzamiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Mujeres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calzado', models.CharField(max_length=50)),
                ('descripcion_calzado', models.CharField(max_length=50)),
                ('talle_calzado', models.IntegerField()),
                ('precio_calzado', models.CharField(max_length=50)),
                ('color_calzado', models.CharField(max_length=20)),
                ('material_calzado', models.CharField(max_length=50)),
                ('disponible_en_stock', models.BooleanField(default=True)),
                ('fecha_lanzamiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Nenas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calzado', models.CharField(max_length=50)),
                ('descripcion_calzado', models.CharField(max_length=50)),
                ('talle_calzado', models.IntegerField()),
                ('precio_calzado', models.CharField(max_length=50)),
                ('color_calzado', models.CharField(max_length=20)),
                ('material_calzado', models.CharField(max_length=50)),
                ('disponible_en_stock', models.BooleanField(default=True)),
                ('fecha_lanzamiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Nenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_calzado', models.CharField(max_length=50)),
                ('descripcion_calzado', models.CharField(max_length=50)),
                ('talle_calzado', models.IntegerField()),
                ('precio_calzado', models.CharField(max_length=50)),
                ('color_calzado', models.CharField(max_length=20)),
                ('material_calzado', models.CharField(max_length=50)),
                ('disponible_en_stock', models.BooleanField(default=True)),
                ('fecha_lanzamiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
