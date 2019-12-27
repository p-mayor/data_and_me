from django.shortcuts import render
from .models import File


def show_genres(request):
    return render(request, "genres.html", {'genres': File.objects.all()})
