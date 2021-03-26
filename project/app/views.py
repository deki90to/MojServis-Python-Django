from django.shortcuts import render, redirect
from . models import *
from . forms import *


def index(request):
	mali_servis = MaliServis.objects.all()

	return render(request, 'index.html', {'mali_servis':mali_servis})

def new(request):
	mali_servis = MaliServis.objects.all()
	form = MaliServisForm()

	if request.method == 'POST':
		form = MaliServisForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	return render(request, 'new.html', {'mali_servis':mali_servis, 'form':form})

def update(request, pk):
	mali_servis = MaliServis.objects.get(pk=pk)
	form = MaliServisForm(instance=mali_servis)

	if request.method == 'POST':
		form = MaliServisForm(request.POST, instance=mali_servis)
		if form.is_valid():
			form.save()
			return redirect('index')

	return render(request, 'update.html', {'mali_servis':mali_servis, 'form':form})

def delete(request, pk):
	mali_servis = MaliServis.objects.get(pk=pk)

	if request.method == 'POST':
		mali_servis.delete()
		return redirect('index')

	return render(request, 'delete.html', {'mali_servis':mali_servis})


