# Generated by Django 3.2.7 on 2022-06-15 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('RoducWeb', '0029_auto_20220615_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('cod_asignatura', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('horas_catedra', models.IntegerField()),
                ('curso', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('cod_auditoria', models.AutoField(primary_key=True, serialize=False)),
                ('tabla', models.CharField(max_length=100)),
                ('accion', models.CharField(max_length=1)),
                ('datos_viejos', models.CharField(max_length=5000)),
                ('datos_nuevos', models.CharField(max_length=5000)),
                ('usuario', models.CharField(max_length=45)),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auditoria_Sesiones',
            fields=[
                ('cod_aud_sesiones', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=45)),
                ('fecha', models.DateTimeField()),
                ('informacion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cabecera_Planilla',
            fields=[
                ('cod_cabecera_planilla', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_clase', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('fecha_vencimiento', models.DateField()),
                ('evaluacion', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_asignatura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('cod_carrera', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
                ('duracion', models.IntegerField()),
                ('titulo_obtenido', models.CharField(max_length=100)),
                ('estado', models.IntegerField(null=True)),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('cod_contenido', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='Instrumento_Evaluacion',
            fields=[
                ('cod_instrumento_evaluacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Metodologia_Ense??anza',
            fields=[
                ('cod_metodologia_ense??anza', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recursos_Auxiliar',
            fields=[
                ('cod_recurso_auxiliar', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol_Usuario',
            fields=[
                ('cod_rol_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=45)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('cod_semestre', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField(null=True)),
                ('fecha_fin', models.DateField(null=True)),
                ('estado', models.IntegerField(null=True)),
                ('alta_usuario', models.CharField(max_length=45, null=True)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('modif_usuario', models.CharField(max_length=45, null=True)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Clase',
            fields=[
                ('cod_tipo_clase', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Eva',
            fields=[
                ('cod_tipo_eva', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo_Autonomo',
            fields=[
                ('cod_trabajo_autonomo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=45)),
                ('contrase??a', models.CharField(max_length=45)),
                ('nombres_del_usuario', models.CharField(max_length=45)),
                ('apellidos_del_usuario', models.CharField(max_length=45)),
                ('direccion_email', models.CharField(max_length=60)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Rol',
            fields=[
                ('cod_usuario_rol', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.carrera')),
                ('cod_rol_usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.rol_usuario')),
                ('cod_usuario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad_Aprendizaje',
            fields=[
                ('cod_unidad_aprendizaje', models.AutoField(primary_key=True, serialize=False)),
                ('numero_unidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_asignatura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos_Utilizados',
            fields=[
                ('cod_trabajos_utilizados', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_cabecera_planilla', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.cabecera_planilla')),
                ('cod_trabajo_autonomo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.trabajo_autonomo')),
            ],
        ),
        migrations.CreateModel(
            name='Recursos_Utilizados',
            fields=[
                ('cod_recursos_utilizados', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_cabecera_planilla', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.cabecera_planilla')),
                ('cod_recurso_auxiliar', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.recursos_auxiliar')),
            ],
        ),
        migrations.CreateModel(
            name='Plan_Estudio',
            fields=[
                ('cod_plan_estudio', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_carrera', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Metodologia_Utilizada',
            fields=[
                ('cod_metodologia_utilizada', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_cabecera_planilla', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.cabecera_planilla')),
                ('cod_metodologia_ense??anza', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.metodologia_ense??anza')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluaciones',
            fields=[
                ('cod_evaluacion', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_cabecera_planilla', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.cabecera_planilla')),
                ('cod_instrumento_evaluacion', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.instrumento_evaluacion')),
                ('cod_tipo_eva', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.tipo_eva')),
            ],
        ),
        migrations.CreateModel(
            name='Contenidos_Dados',
            fields=[
                ('cod_contenidos_dados', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_cabecera_planilla', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.cabecera_planilla')),
                ('cod_contenido', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.contenido')),
            ],
        ),
        migrations.AddField(
            model_name='contenido',
            name='cod_unidad_aprendizaje',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.unidad_aprendizaje'),
        ),
        migrations.AddField(
            model_name='carrera',
            name='cod_facultad',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.facultad'),
        ),
        migrations.AddField(
            model_name='cabecera_planilla',
            name='cod_tipo_clase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.tipo_clase'),
        ),
        migrations.AddField(
            model_name='cabecera_planilla',
            name='cod_usuario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.usuario'),
        ),
        migrations.CreateModel(
            name='Asignatura_Usuario',
            fields=[
                ('cod_asignatura_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.IntegerField()),
                ('alta_usuario', models.CharField(max_length=45)),
                ('alta_fecha', models.DateTimeField(auto_now_add=True)),
                ('modif_usuario', models.CharField(max_length=45)),
                ('modif_fecha', models.DateTimeField(auto_now=True)),
                ('cod_asignatura', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.asignatura')),
                ('cod_usuario_rol', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.usuario_rol')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='cod_carrera',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.carrera'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='cod_plan_estudio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.plan_estudio'),
        ),
        migrations.AddField(
            model_name='asignatura',
            name='cod_semestre',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RoducWeb.semestre'),
        ),
    ]
