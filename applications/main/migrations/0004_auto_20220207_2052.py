# Generated by Django 3.0.5 on 2022-02-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220207_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='receta',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
