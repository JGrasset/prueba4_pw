# Generated by Django 3.2.4 on 2021-06-14 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
    ]