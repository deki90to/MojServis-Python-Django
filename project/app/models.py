from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from datetime import datetime

class Automobil(models.Model):
	marka = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.marka}'

class MaliServis(models.Model):
	ms_automobila = models.ForeignKey('Automobil', on_delete=models.CASCADE)
	tablica = models.CharField(max_length=10, blank=True, null=True)
	kilometraza = models.IntegerField()
	ulje = models.CharField(max_length=30)
	filter_ulja = models.BooleanField()
	filter_goriva = models.BooleanField()
	filter_vazduha = models.BooleanField()
	filter_kabine = models.BooleanField()
	info = models.TextField(max_length=500, blank=True, null=True)
	date = models.DateTimeField(default=datetime.now, null=True)

	def __str__(self):
		return f'{self.ms_automobila}, {self.tablica}, {self.kilometraza}, {self.ulje}, {self.info}'

	class Meta:
		ordering = ['-date']

class VelikiServis(models.Model):
	vs_automobila = models.ForeignKey('Automobil', on_delete=models.CASCADE)
	tablica = models.CharField(max_length=10, blank=True, null=True)
	kilometraza = models.IntegerField()
	kais = models.BooleanField()
	lanac = models.BooleanField()
	zatezac = models.BooleanField()
	roler = models.BooleanField()
	spaner = models.BooleanField()
	pumpa_vode = models.BooleanField()
	info = models.TextField(max_length=500, blank=True, null=True)
	date = models.DateTimeField(default=datetime.now, null=True)

	def __str__(self):
		return f' {self.vs_automobila}, {self.kilometraza}, {self.info}'

	class Meta:
		ordering = ['-date']