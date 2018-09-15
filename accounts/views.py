# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.
def index(request):
    """ Return the index.html file (Home) """
    return render(request, 'index.html')
    
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "YOu have now logged out. See you soon") # a mesage to the user to say they have logged out
    return redirect(reverse('index'))  # once logged out will return to the index page
    