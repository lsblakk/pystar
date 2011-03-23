#!/usr/bin/env python

'''
Tests for the 'polls' application.  Call using:

    ./manage.py test
'''

# called automatically by ./manage.py test; no harm though.
from django.test.utils import setup_test_environment
setup_test_environment()

# uses the new 'unittest2' improved testing framework
from django.utils import unittest
from django.test.client import Client

## Tests

class Text_example(unittest.TestCase):
    def test_testing_is_sane(self):
        pass

class Test_urls(unittest.TestCase):
    def test_root_responds(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)



class Test_models(unittest.TestCase):
    pass


