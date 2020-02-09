from django.db import models
from clasificacion.models import Clasificacion
from grupo.models import Grupo
from periodo.models import Periodo

# Create your models here.
class Elemento(models.Model):
	name = models.CharField(max_length=50)
	masa_atomica = models.FloatField(default=None)
	simbolo = models.CharField(max_length=10,default=None)
	clasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE)
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
	

	def __str__(self):
	    return self.name

	class Meta:
	    ordering = ('name',)


