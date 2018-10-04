# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse 


# Create your views here.
""" This renders everything within the cart """
def view_cart(request):
    render(request, "cart.html")

""" Add a quantity of the specified product to the cart, IT WHEN YOU CLICK ON THE ADD TO CART BUTTON"""    
def add_to_cart(request):
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
def adjust_cart(request, id):
    """ Adjust the quantity of a product to the specified amount """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    