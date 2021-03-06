# Generated by Django 3.2.7 on 2022-05-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoducWeb', '0003_auditoria_auditoria_sesiones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('cod_facultad', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_fundacion', models.DateField()),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
