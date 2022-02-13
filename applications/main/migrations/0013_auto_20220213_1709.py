# Generated by Django 3.0.5 on 2022-02-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220207_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(max_length=255, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='difficult',
            field=models.CharField(blank=True, choices=[('0', 'Facil'), ('1', 'Medio'), ('2', 'Dificil')], max_length=1, null=True, verbose_name='Dificultad'),
        ),
    ]