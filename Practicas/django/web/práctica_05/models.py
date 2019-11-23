from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Musico(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    fnac = models.DateField()
    instrumento = models.CharField(max_length=20,
        choices = [('guitarra', 'guitarra'), ('bajo', 'bajo'), ('bateria', 'bateria'), ('violin', 'violin'), ('piano', 'piano'),]
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class GrupoMusical(models.Model):
    nombre = models.CharField(max_length=50)
    creacion = models.DateField()
    estilo = models.CharField(max_length=20,
        choices = [('rock', 'rock'), ('pop', 'pop'), ('indie', 'indie'), ('metal', 'metal'), ('r&b', 'r&b'), ('alternativa', 'alternativa'),]
    )
    miembros = models.ManyToManyField(Musico)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Album(models.Model):
    artista = models.ForeignKey(GrupoMusical, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    lanzamiento = models.DateField()
    estrellas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
