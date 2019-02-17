# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
import core.scripts.terminal as wetty
from django.contrib.auth.models import User
from core.scripts import judgeCode as jc
from django.shortcuts import render, redirect
from django.http import HttpResponse

tpid = None
tport = None

# Create your views here.
def signup(request):
    return render(request, 'core/signup.html')

@xframe_options_sameorigin
def ide(request):
    global tport
    tport = wetty.getUnusedPort()
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
#           HANDLING WETTY REQUESTS               #
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
            tpid = wetty.terminal('admin', tport)
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
            print('closed wetty server: ' + str(tport))
            return HttpResponse('')
        except Exception as e:
            print('except: ' + e)
            return HttpResponseServerError(content=b'%s' % e.message)