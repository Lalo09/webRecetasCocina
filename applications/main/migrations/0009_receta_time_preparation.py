# Generated by Django 3.0.5 on 2022-02-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20220207_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='time_preparation',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tiempo de preparacion'),
        ),
    ]
