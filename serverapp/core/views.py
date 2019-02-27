# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
import core.scripts.terminal as cotty
from django.contrib.auth.models import User
from core.scripts import judgeCode as jc
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Signup imports
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

tpid = None
tport = None

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

@xframe_options_sameorigin
def ide(request):
    global tport
    tport = cotty.getUnusedPort()
    if request.is_ajax():
        code = request.POST
        jc.postCode(code, '35')
    print("user port is: " + str(tport))
    return render(request, "core/ide/ide.html")

def settings(request):
    return render(request, 'core/settings.html')

def index(request):
    return render(request, 'core/index.html')

def problems(request):
    return render(request, 'core/problems.html')

def scoreboard(request):
    return render(request, 'core/scoreboard.html')


###################################################
#                                                 #
#           HANDLING cotty REQUESTS               #
#                                                 #
###################################################

@csrf_exempt
@xframe_options_sameorigin
def makeTerminal(request):
    global tpid, tport
    print("Making terminal.")
    if request.is_ajax():
        try:
            print('allocating to user...')
            tpid = cotty.terminal('admin', tport)
            terminal_port = tpid.makeServer()
            return HttpResponse(str(terminal_port))
        except Exception as e:
            return HttpResponseServerError(content=b'%s' % e.message)

@csrf_exempt
@xframe_options_sameorigin
def destroyTerminal(request):
    global tpid, tport
    print("Destroying terminal.")
    if request.is_ajax():
        try:
            tpid.terminate()
            print('closed cotty server: ' + str(tport))
            return HttpResponse('')
        except Exception as e:
            print('except: ' + e)
            return HttpResponseServerError(content=b'%s' % e.message)
