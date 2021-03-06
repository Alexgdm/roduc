# Generated by Django 3.2.7 on 2022-05-19 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoducWeb', '0006_auto_20220519_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('cod_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
                ('duracion', models.IntegerField()),
                ('titulo_obtenido', models.CharField(max_length=100)),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_faculad', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.facultad')),
            ],
        ),
    ]
