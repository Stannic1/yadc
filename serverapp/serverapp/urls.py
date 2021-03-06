"""serverapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views as core_views

# Login Logout Imports
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    # If no path, default to index
    url(r'^$', core_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^ide/$', core_views.ide, name='ide'),
    url(r'^ide/makeTerminal', core_views.makeTerminal, name='makeTerminal'),
    url(r'^ide/endTerminal', core_views.destroyTerminal, name='endTerminal'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^index/$', core_views.index, name='index'),
    url(r'^problems/$', core_views.problems, name='problems'),
    url(r'^scoreboard/$', core_views.scoreboard, name='scoreboard'),
    path('accounts/', include('django.contrib.auth.urls')),
]
