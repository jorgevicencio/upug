from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class forofo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    equipofavorito = models.CharField(max_length=3, null=True)


class equipos(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    codigo_equipo = models.CharField(max_length=3, null=True)
    ciudad = models.CharField(max_length=50, null=True)
    partidos_jugados = models.IntegerField(null=True) 
    partidos_ganados= models.IntegerField(null=True)
    partidos_empatados= models.IntegerField(null=True)
    goles_convertidos = models.IntegerField(null=True)
    goles_recibidos = models.IntegerField(null=True)
    diferencia_de_gol = models.IntegerField(null=True)
    tarjetas_amarillas = models.IntegerField(null=True)
    tarjetas_rojas = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class jugadores(models.Model):
    nombrenacionalidad = models.CharField(max_length=50, null=True)
    equipoactual = models.ForeignKey(equipos, on_delete=models.CASCADE)
    traspasadodesde = models.CharField(max_length=50, null=True)
    partidos_jugados = models.IntegerField(null=True)
    goles = models.IntegerField(null=True)
    asistencias = models.IntegerField(null=True)
    tarjetas_amarillas = models.IntegerField(null=True)
    tarjetas_rojas = models.IntegerField(null=True)

    def __str__(self):
        return self.name