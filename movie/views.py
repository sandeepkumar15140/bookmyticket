from django.shortcuts import render
from .models import movies_detail

def movie(request):
    mov = movies_detail.objects
    return render(request, 'movies.html', {'mov':mov})
