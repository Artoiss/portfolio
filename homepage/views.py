from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'homepage/index.html')

def projects(request):
    return render(request, 'homepage/projects.html')
