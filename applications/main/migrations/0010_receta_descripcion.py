# Generated by Django 3.0.5 on 2022-02-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_receta_time_preparation'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='descripcion'),
        ),
    ]
