# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.conf import settings
import datetime
import stripe

stripe.api_key = settings.STRIPE_SECRET

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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=999,
                    currency="USD",
                    description=form.cleaned_data['email'],
                    card=form.cleaned_data['stripe_id'],
                )
                if customer.paid:
                    form.save()
                    user = auth.authenticate(email=request.POST.get('email'),
                                             password=request.POST.get('password1'))
                    if user:
                        auth.login(request, user)
                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))
                    else:
                        messages.error(request, "unable to log you in at this time!")
                else:
                    messages.error(request, "We were unable to take a payment with that card!")
            except stripe.error.CardError, e:
                messages.error(request, "Your card was declined!")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()
 
    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
 
    return render(request, 'registration.html', args)
        

#def profile(request):
#    """ The users profile page"""
#    user = User.objects.get(email=request.user.email)
#    return render(request, 'profile.html', {"profile": user})
    
"""  return the current profile """    
def profile(request):
    return render(request, 'profile.html')
        