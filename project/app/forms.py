from django import forms
from . models import *

class MaliServisForm(forms.ModelForm):
	class Meta:
		model = MaliServis
		fields = (
			'user',
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
			'ms_automobila':'Brend Automobila',
			'tablica':'',
			'kilometraza':'',
			'ulje':'',
			'info':''}			
		
		widgets = {
			'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			# 'ms_automobila':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marka'}),
			'tablica':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tablica'}),
			'kilometraza':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraza'}),
			'ulje':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ulje'}),
			'info':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vise informacija'}),
		}



# class VelikiServisForm(forms.ModelForm):
# 	class Meta:
# 		fields = (
# 			'vs_automobila',
# 			'tablica',
# 			'kilometraza',
# 			'kais',
# 			'lanac',
# 			'zatezac',
# 			'roler',
# 			'spaner',
# 			'pumpa_vode',
# 			'info')