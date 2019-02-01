# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from core.scripts import judgeCode as jc
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Signup imports
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=raw_password)
            login(request, user)
            # Redirect back to index
            return redirect('/index')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
    # return render(request, 'core/signup.html')

def ide(request):
    if request.is_ajax():
        code = request.POST
        jc.postCode(code, '35')
    return render(request, "core/ide/ide.html")

def settings(request):
    return render(request, 'core/settings.html')

def index(request):
    return render(request, 'core/index.html')

def problems(request):
    return render(request, 'core/problems.html')

def scoreboard(request):
    return render(request, 'core/scoreboard.html')