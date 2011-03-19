

.. _dep-django-label:

django
--------------------

.. _dep-django-what-label:

What is ``django``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django is the most-popular web-development framework written in Python.



.. _dep-django-why-label:

Why do I need ``django``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For building our voting application!  


.. _dep-django-how-label:

Get ``django``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We don't want to install django system wide, but rather in our local
virtualenv.  

::

    # Create and activate a virtualenv
    virtualenv --no-site-packages pystar
    . testenv/bin/activate  # windows -> . testenv\Scripts\activate.bat
    pip install django



.. _django-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    $ python
    >>> import django

The whole process should look something like::

    Gregg-Linds-MacBook-Pro:gits gregg$ pwd
    /Users/gregg/gits
    Gregg-Linds-MacBook-Pro:gits gregg$ virtualenv --no-site-packages pystar2
    New python executable in pystar2/bin/python
    Installing setuptools.............done.
    Gregg-Linds-MacBook-Pro:gits gregg$ . pystar2/bin/activate
    (pystar2)Gregg-Linds-MacBook-Pro:gits gregg$ pip install django
    Downloading/unpacking django
      Downloading Django-1.2.5.tar.gz (6.4Mb): 6.4Mb downloaded
      Running setup.py egg_info for package django
    Installing collected packages: django
      Running setup.py install for django
        changing mode of build/scripts-2.6/django-admin.py from 644 to 755
        changing mode of /Users/gregg/gits/pystar2/bin/django-admin.py to 755
    Successfully installed django
    Cleaning up...
    (pystar2)Gregg-Linds-MacBook-Pro:gits gregg$ python
    Python 2.6.1 (r261:67515, Jun 24 2010, 21:47:49) 
    [GCC 4.2.1 (Apple Inc. build 5646)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>> 
