from django import forms
from . models import *

class MaliServisForm(forms.ModelForm):
	class Meta:
		model = MaliServis
		fields = (
			'ms_automobila',
			'tablica',
			'kilometraza',
			'ulje',
			'filter_ulja',
			'filter_goriva',
			'filter_vazduha',
			'filter_kabine',
			'info')

		labels = {
			'ms_automobila':'',
			'tablica':'',
			'kilometraza':'',
			'ulje':'',
			# 'filter_ulja':'',
			# 'filter_goriva':'',
			# 'filter_vazduha':'',
			# 'filter_kabine':'',
			'info':''}			
		
		widgets = {
			# 'ms_automobila':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marka'}),
			'tablica':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tablica'}),
			'kilometraza':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraza'}),
			'ulje':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ulje'}),
			# 'filter_ulja':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filter ulja'}),
			# 'filter_goriva':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filter goriva'}),
			# 'filter_vazduha':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filter vazduha'}),
			# 'filter_kabine':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Filter kabine'}),
			'info':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vise informacija'}),
		}




