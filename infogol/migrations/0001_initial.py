# Generated by Django 3.0.7 on 2020-06-16 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('codigo_equipo', models.CharField(max_length=3, null=True)),
                ('ciudad', models.CharField(max_length=50, null=True)),
                ('partidos_jugados', models.IntegerField(null=True)),
                ('partidos_ganados', models.IntegerField(null=True)),
                ('partidos_empatados', models.IntegerField(null=True)),
                ('goles_convertidos', models.IntegerField(null=True)),
                ('goles_recibidos', models.IntegerField(null=True)),
                ('diferencia_de_gol', models.IntegerField(null=True)),
                ('tarjetas_amarillas', models.IntegerField(null=True)),
                ('tarjetas_rojas', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrenacionalidad', models.CharField(max_length=50, null=True)),
                ('traspasadodesde', models.CharField(max_length=50, null=True)),
                ('partidos_jugados', models.IntegerField(null=True)),
                ('goles', models.IntegerField(null=True)),
                ('asistencias', models.IntegerField(null=True)),
                ('tarjetas_amarillas', models.IntegerField(null=True)),
                ('tarjetas_rojas', models.IntegerField(null=True)),
                ('equipoactual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infogol.equipos')),
            ],
        ),
    ]
