# Generated by Django 3.0.5 on 2022-02-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_receta_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='descripcion'),
        ),
    ]
