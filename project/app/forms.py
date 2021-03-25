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