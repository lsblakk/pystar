.. _badge_twitter:

Build a Twitter Client
----------------------------

#.  (Grab a group guide to help out!  This is rough and imcomplete) 
#.  http://search.twitter.com/api/
#.  ::

        >>> import json
        >>> import urllib
        >>> q = "http://search.twitter.com/search.json?q=pystar"
        >>> print urllib.urlopen(q)
        >>> print urllib.urlopen(q).read()
        >>> d = json.loads(urllib.urlopen(q))
        >>> print d['results'][0]

#.  Discuss ``urllib``, ``json``, etc.
#.  Do some other kinds of searches.
#.  Continue from here with https://github.com/jesstess/BostonPythonWorkshop/tree/master/twitter_api
