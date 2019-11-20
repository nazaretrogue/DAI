from django.db import models

# Create your models here.
class Musico(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    fnac = models.DateField()
    instrumento = models.CharField(
        choices = ('guitarra', 'bajo', 'bateria', 'violin', 'piano'),
        help_text = "Seleccione el género")
    )

class Album(models.Model):
    artista =
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    estrellas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class GrupoMusical(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateField()
    estilo = models.CharField(
        choices = ('rock', 'pop', 'indie', 'metal', 'r&b', 'alternativa'),
        help_text = "Seleccione el género")
    )
    miembros = models.ManyToManyField(Musico)
