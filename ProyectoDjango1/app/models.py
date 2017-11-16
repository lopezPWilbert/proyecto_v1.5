"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User


class Usuario_m(models.Model):
	Nombre = models.OneToOneField(User,on_delete=models.CASCADE)
	Telefono = models.IntegerField(null=True, blank=True)
	Direccion = models.CharField(max_length=100,null=True, blank=True)
	Avatar = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

	def __unicode__(self):
		return self.Nombre.username



 
class Denuncia_m(models.Model):
	user=models.ForeignKey(User)
	titulo=models.CharField(max_length=50)
	descripcion=models.TextField()
	latitud=models.FloatField()
	longitud=models.FloatField()
	
	def __unicode__(self):
		return self.titulo

class imagenes_m(models.Model):
    denunciaA=models.ForeignKey(Denuncia_m, null=True, blank=True)
    imagen=models.FileField(upload_to='img/%Y/%m/%d',null=True, blank=True)

class videos_m(models.Model):
    denunciaB=models.ForeignKey(Denuncia_m, null=True, blank=True)
    video=models.FileField(upload_to='img/%Y/%m/%d',null=True, blank=True)
	
class Comentario_m(models.Model):
	user=models.ForeignKey(User)
	denuncia=models.ForeignKey(Denuncia_m,null=True, blank=True)
	comentario=models.CharField(max_length=250)
	
	def __unicode__(self):
		return self.comentario

