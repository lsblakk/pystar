

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

.. code-block:: bash

    # In your home directory create and activate a virtualenv
    cd ~
    virtualenv --no-site-packages pystar
    cd pystar 
    source bin/activate  # windows -> pystar\Scripts\activate.bat
    
    pip install django

    # to deactivate the virtualenv you would do
    # but don't do this now :)
    deactivate

.. _django-verify-label:

Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python
    >>> import django
    
    # to quit the python prompt do
    exit()

.. _django-app-create-label:

Verify you can create a new Django app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a folder on the desktop called ``django_projects``
Open a new Terminal window and type the following: 

..  code-block:: bash

   # with virtualenv pystar activated, see above, and the virtualenv page
   mkdir django_projects
   cd django_projects
   django-admin.py startproject myproject

Both commands should provide no output.
Once that's finished, type the following in the Terminal window: 

.. code-block:: bash

    cd myproject
    python manage.py runserver

    # output should look like this
    Validating models...
    0 errors found

    Django version 1.2.5, using settings 'myproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.


In your browser, go to http://127.0.0.1:8000/ 

.. code-block:: bash

    # in your Terminal window you should see something like:
    [19/Mar/2011 19:19:26] "GET / HTTP/1.1" 200 2057

Back in the Terminal window where you ran python manage.py runserver, 
type control-c to kill the server. 

Congratulations, you have run your first Django app!

The whole process should look something like:

.. code-block:: bash

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
    >>> exit()
    mkdir django_projects
    cd django_projects
    django-admin.py startproject 
    cd myproject
    python manage.py runserver
    Validating models...
    0 errors found
    
    Django version 1.2.5, using settings 'myproject.settings'
    Development server is running at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    [19/Mar/2011 19:19:26] "GET / HTTP/1.1" 200 2057


