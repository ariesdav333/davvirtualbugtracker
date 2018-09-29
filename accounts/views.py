# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """ Return the index.html file (Home) """
    return render(request, 'index.html')
    
def about(request):
    """ Return the about.html filr (About) """
    return render(request, 'about.html')

@login_required()  
def logout(request):
    """ Log the user out """
    auth.logout(request)
    messages.success(request, "You have now logged out. Please visit us again") # a mesage to the user to say they have logged out
    return redirect(reverse('index'))  # once logged out will return to the index page


def login(request):
    """ Log user in to a page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        """ Will test the users credentials to see if the login is correect with a message to the user """
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have now logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "You username or password is incorrect")
                
                
            
    else:
        login_form = UserLoginForm()    # just defaults to the normal User Login screen waiting for input
    return render(request, 'login.html', {"login_form": login_form})
    
    
def registration(request):
    """ Render the registration page """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
                                     
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register the account at this time")
    else:    
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {
        "registration_form": registration_form})
        
        
def user_profile(request):
    """ The users profilr page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
        