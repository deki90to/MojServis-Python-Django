from django import forms
from . models import *

class MaliServisForm(forms.ModelForm):
	class Meta:
		model = MaliServis
		fields = (
			'user',
			'ms_automobila',
			'model',
			'tablica',
			'kilometraza',
			'ulje',
			'filter_ulja',
			'filter_goriva',
			'filter_vazduha',
			'filter_kabine',
			'info',
			'slike',
			)

		labels = {
			'ms_automobila':'Brend',
			'model':'',
			'tablica':'',
			'kilometraza':'',
			'ulje':'',
			'info':''
			}			
		
		widgets = {
			'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			'tablica':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tablica'}),
			'kilometraza':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraza'}),
			'ulje':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ulje'}),
			'info':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vise informacija'}),
			'model':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Model'}),
		}