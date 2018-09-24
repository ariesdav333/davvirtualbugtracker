# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    
    """ Lets define Product test against our models """
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')