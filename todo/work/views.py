from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages

from .forms import WorkForm, UpdateWorkForm
from .models import *

# Create your views here.

def home(request):
    works = Work.objects.all()

    form = WorkForm()

    if request.method == 'POST':
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')

    context = {
        'works': works,
        'form': form
    }
    return render(request, 'work/home.html', context)


def update(request, id):
    work = Work.objects.get(id=id)
    form = UpdateWorkForm(instance=work)
    if request.method == 'POST':
        form = UpdateWorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            messages.success(request, 'Work Updated Successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'work/update.html', context)


def delete(request, id):
    work = Work.objects.get(id=id)
    if request.method == 'POST':
        work.delete()
    return redirect('home')