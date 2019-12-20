from django.shortcuts import render
from .models import movies_detail
from .models import event_detail

def movie(request):
    mov = movies_detail.objects
    return render(request, 'movies.html', {'mov':mov})

def event(request):
    eve = event_detail.objects
    return render(request, 'events.html', {'eve':eve})

