# Generated by Django 4.2.5 on 2023-10-12 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBalti', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conjunto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='catalogo', width_field='80 px'),
        ),
    ]
