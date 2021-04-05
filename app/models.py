from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from datetime import datetime
from django.contrib.auth.models import User

class Automobil(models.Model):
	marka = models.CharField(max_length=30)

	def __str__(self):
		return f'{self.marka}'

class MaliServis(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	ms_automobila = models.ForeignKey('Automobil', on_delete=models.CASCADE)
	model = models.CharField(max_length=20, null=True, blank=True)
	tablica = models.CharField(max_length=10, blank=True, null=True)
	kilometraza = models.IntegerField()
	ulje = models.CharField(max_length=30)
	filter_ulja = models.BooleanField()
	filter_goriva = models.BooleanField()
	filter_vazduha = models.BooleanField()
	filter_kabine = models.BooleanField()
	info = models.TextField(max_length=1000, blank=True, null=True)
	date = models.DateTimeField(default=datetime.now, null=True)


	def __str__(self):
		return f'{self.user}, {self.ms_automobila}, {self.model}, {self.tablica}, {self.kilometraza}, {self.ulje}, {self.info}'

	class Meta:
		ordering = ['-date']