# Generated by Django 3.2.7 on 2022-05-21 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoducWeb', '0013_plan_estudio_cod_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='estado',
            field=models.IntegerField(null=True),
        ),
    ]
