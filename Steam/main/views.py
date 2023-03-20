from multiprocessing import context
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from . import forms

def home(request):
    return render(request, 'home.html')

def games(request):
    games = Paginator(Hry.objects.all(), 15)
    page = request.GET.get('page')
    items_in_page = games.get_page(page)
    context = {
        'hry': items_in_page,
    }
    return render(request, 'hry.html', context)

def game(request, id):
    game = Hry.objects.get(idhry=id)
    recenze = Paginator(Hodnoceni.objects.filter(hry_idhry=id), 20)
    page = request.GET.get('page')
    items = recenze.get_page(page)
    context = {
        'hra': game,
        'reviews': items,
    }
    return render(request, 'hra.html', context)

def publisher(request, id):
    publisher = Publisher.objects.get(idpublisher=id)
    context = {
        'publisher': publisher
    }
    return render(request, 'publisher.html', context)

def add(request):
    submitted = False
    if request.method == "POST":
        form = forms.add_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add?submitted=True')
    else:
        form = forms.add_form()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'add.html', context)

def update(request, id):
    pass

def delete(request, id):
    HryHasUzivatele.objects.filter(hry_idhry=id).delete()
    HryHasZanr.objects.filter(hry_idhry=id).delete()
    Hry.objects.get(idhry=id).delete()
    return HttpResponseRedirect('/games')