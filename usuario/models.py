from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	usuario= models.OneToOneField(User)
	telefono= models.CharField(max_length=20)

	def __str__(self):
		return "%s %s - %s" %(
			self.nombre,
			self.correo,
			self.usuario)
