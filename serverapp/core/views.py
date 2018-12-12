# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return render(request, 'core/signup.html')

def ide(request):
    return render(request, 'core/ide.html')

def settings(request):
    return render(request, 'core/settings.html')

def index(request):
    return render(request, 'core/index.html')

def problems(request):
    return render(request, 'core/problems.html')

def scoreboard(request):
    return render(request, 'core/scoreboard.html')
