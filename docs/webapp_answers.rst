.. _webapp_answers:

Answers for Webapp Questions
--------------------------------------

..  danger::

    Looking at these answers **too soon** can cause 
    indigestion, headaches, hair loss, mass panic
    and other side-effects.  Be cautious!  Think 
    through the question **first**!  

    Remember

    - you can do this!
    - effort matters!




.. _webapp_answers_verify_shutdown:

How To Verify Shutdown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

go to http://127.0.0.1:8080/ and see if you get a 404, or 500!


.. _webapp_answers_single_quote:

Single Quote
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Recall (or know!) that python can single-quote, double quote, or triple quote strings::

    SECRET_KEY="that's my string"

or::

    SECRET_KEY='''that's my string'''


.. _webapp_answers_database_db_exists:

Does ``database.db`` exist?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It shouldn't!  Use ``ls`` to find out!


.. _webapp_answers_django_standard_apps:

Why are the standard apps standard?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* They are useful for most web projects.
* They are tedious to write, or hard to code correctly or both.


By default, ``INSTALLED_APPS`` contains the following apps, all of which come with Django:

* django.contrib.auth -- An authentication system.
* django.contrib.contenttypes -- A framework for content types.
* django.contrib.sessions -- A session framework.
* django.contrib.sites -- A framework for managing multiple sites with one Django installation.
* django.contrib.messages -- A messaging framework.

These applications are included by default as a convenience.  


.. _webapp_answers_django_magical:

Does this all seem magical?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes, this is all somewhat magical.  Eventually, that should start to worry
you, but for now, accept that it mostly works, most of the time. 



.. _webapp_answers_database_db_exists_after_sync:

Does ``database.db`` exist *now*?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It should!  That is one of the magical bits of ``dbsync``  Use ``ls`` to find out!


.. _webapp_answers_save_my_work:

How Do I save my work?
---------------------------------------

We've done something! Let's share it with the world.

We'll do that with ``git`` and ``Github``. On your own computer, get to a Terminal or a GitBash.

#.  ``cd`` to get into the ``myproject`` directory. If it's a fresh Terminal, this is what you'll do:

    .. code-block:: bash

         cd ~/django_projects/myproject

#.  Is this new project?  If so:


    #. create a git repository in the project directory:

        .. code-block:: bash

            # in myproject
            git init

    #   Tell git to ignore any files that end with .pyc (compiled python code) when we push
        to our repo so we need to add that to ``.git/info/exclude``:

        .. code-block:: bash

            # in myproject directory
            gedit .git/info/exclude
            
            # add this line to the end of the file
            .pyc

    #   Create your project on GitHub.

        # Go to http://github.com/ and create a new repository called "myproject". On the main dashboard page, click on "New Repository" fill out the necessary information. 

#   Add all your files to the repo, in the local directory:

    .. code-block:: bash

        git add -A

    Now git is aware of your files.  Use ``git status`` to see them there in
    the *staging* area (the index).  

#   ``git commit`` to ``commit`` those files:

    .. code-block:: bash

        git commit -m "Initial commit of django app project from the PyStar workshop"

#   Connect the remote github repo to your local one, and use ``git push`` to push those up to your Github repository:

    .. code-block:: bash

        git remote add origin git@github.com:username/myproject.git
        git push origin master

#   Go to your Github account in your browser. Find the ``myproject`` repository. Do you see your files?




.. _webapp_answers_test_my_work:

How Do I test my work?
---------------------------------------
