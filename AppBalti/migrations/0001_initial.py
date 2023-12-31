# Generated by Django 4.2.5 on 2023-09-21 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bombacha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('articulo', models.IntegerField()),
                ('talle', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=40)),
                ('tipo_bombacha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Conjunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('articulo', models.IntegerField()),
                ('talle', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=40)),
                ('tipo_taza', models.CharField(max_length=20)),
                ('tipo_bombacha', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dormir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('articulo', models.IntegerField()),
                ('talle', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=40)),
                ('tipo_prenda', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Puntos_De_Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comercio', models.CharField(max_length=40)),
                ('provincia', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=70)),
                ('domicilio', models.CharField(max_length=70)),
                ('red_social', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
