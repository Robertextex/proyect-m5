from django.db import models
from django.urls import reverse


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50, primary_key=True)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=7)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

class gestionTickets(models.Model):
	solicitud= models.CharField(max_length=200)
	incidente= models.CharField(max_length=200)
	prioridad= models.CharField(max_length=2)

def __str__(self):
		return self.prioridad

class responsablesAtencion(models.Model):
	atencionChat = models.CharField(max_length=30)
	atencionMesa = models.CharField(max_length=30)
	soporteTecnico = models.CharField(max_length=30)

def __str__(self):
		return self.soporteTecnico

class contactoTipo(models.Model):
	individuo = models.CharField(max_length=30)
	organizacion = models.CharField(max_length=30)

def __str__(self):
		return self.individuo
