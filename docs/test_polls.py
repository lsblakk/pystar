#!/usr/bin/env python

'''
Tests for the 'polls' application.  Call using:

    ./manage.py test polls
'''

# called automatically by ./manage.py test; no harm though.
from django.test.utils import setup_test_environment
setup_test_environment()

# uses the new 'unittest2' improved testing framework, django 1.3+
from django.utils import unittest 

from django.test.client import Client


## utilities

import datetime
import random


models_importable = False
try:
    from polls.models import Choice,Poll
    models_importable = True
except ImportError:
    pass


    
opinions = ['HEINOUS!', 'suxxors', 'rulez!', 
'AWESOME!', 'righTEOUS', 'HAVE MY BABY!!!!',
'BEYOND METAL','SUCKS','RULES', 'TOTALLY RULES']

band_names = '''
Abonos Meshuggah Xasthur Silencer Fintroll Beherit Basilisk Cryptopsy
'''.strip().split()


def setup_metal():
    random.seed(2929485983)  # so it will always make the same polls
    def make_metal_poll(bandname,opinions):
        pub = datetime.datetime.now()
        marks = '?' * random.randint(1,5)
        question = bandname + marks
        chosen = random.sample(opinions,5)
        choices = list()
        for c in chosen:
            votes = random.randint(1,1000)
            choices.append(Choice(choice=c,votes=votes))
        
        p = Poll(question=bandname,pub_date=pub)
        p.save()
        p.choice_set=choices
        return p

    polls = [make_metal_poll(band,opinions) for band in band_names]
    return polls

## Tests

''' (r'^polls/$', 'polls.views.index'),
 (r'^polls/(\d+)/$', 'polls.views.detail'),
 (r'^polls/(\d+)/results/$', 'polls.views.results'),
 (r'^polls/(\d+)/vote/$', 'polls.views.vote'),'''

class Text_example(unittest.TestCase):
    def test_testing_is_sane(self):
        self.assertEqual(1,1)

def get(url):
    c = Client()
    response = c.get(url)
    return response


class Test_urls(unittest.TestCase):
    def test_root_responds(self):
        c = Client()
        response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response.status_code, 200)

    def test_root_responds(self):
        response = get('/')
        self.assertEqual(response.status_code, 200)

    def test_poll_responds(self):
        response = get('/polls/')
        self.assertEqual(response.status_code, 200)


class Test_index(unittest.TestCase):
    pass
    '''which displays the latest 5 
poll questions in the system, separated by commas, according to publication date. '''
    

class Test_voting(unittest.TestCase):
    def setUp(self):
        if models_importable:
            self.polls = setup_metal()
        else:
            self.polls=None
    def test_vote(self):
        r = response = get('/polls/1')
        print r.__dict__

    def test_vote_up_raises_vote_by_one(self):
        if not models_importable :
            self.assertFalse()

    def test_vote_down_lowers_vote_by_one(self):
        if not models_importable :
            self.assertTrue()
    
class Test_models(unittest.TestCase):
    def setUp(self):
        if models_importable :
            self.polls = setup_metal()
        else:
            self.polls=None
    
    def test_poll_has_right_fields(self):
        self.assertFalse(True)

    def test_choice_has_right_fields(self):
        self.assertFalse(True)


## polls need to have pubdate and text
## choices need text and votes

## also choices need a 'is today' method.

## templates!
'''
Usually when I go about testing a Django application, there are 3 major parts that I test. Models, Views, and Template Tags. Templates are hard to test, and are generally more about aesthetics than code, so I tend not to think about actually testing Templates. This should cover most of the parts of your application that are standard. Of course, if your project has utils, forms, feeds, and other things like that, you can and should probably test those as well!

/ lives
something good at slash!

/other/lives 
something is good there!


try import models...
except....
assert false!



'''


