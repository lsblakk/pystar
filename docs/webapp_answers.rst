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


.. _webapp_answers_dev_server_still_works:

Why does the dev server still work when settings.py has been deleted?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because ``settings.pyc`` still exists, and that's what the machine is actually looking at when you run the code that runs the dev server. That's why the dev server does not work when you also delete ``settings.pyc``. Now the computer has no idea what you're talking about, since the original code and the compiled byte code are both gone.



.. _webapp_answers_database_db_exists_after_sync:

Does ``database.db`` exist *now*?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It should!  That is one of the magical bits of ``dbsync``.  Use ``ls`` to find out!



.. _webapp_answers_sqlite_one_writer_implications:

What are the Implications of Sqlite only Handling One Writer?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* performance is blocked by how fast that one writer can write
* multiple processes can clobber each others' data.



.. _webapp_answers_why_testing_matters:

Why Does Testing Matter?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Among other reasons:

* ensure that the features actually work as expected.
* help make it clear what "as expected" actually means.
* stop code changes from breaking things that used to work.
* keep code split into reasonable, understandable chunks
  ("if I can't figure out how to test it, it's probably doing to much!").



.. _webapp_answers_why_not_save_database_db:

Why Don't We Commit ``database.db``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Becuase ``database.db`` is just a 'test database' and doesn't have anything
"real" in it, we don't care about it.  Generally files that are 'built', like
``.pyc`` files, the build html files of this book, and the like aren't put
under version control.  


.. _webapp_answers_is_polls_importable:

Is Polls Importable?
^^^^^^^^^^^^^^^^^^^^^^^^^^

::
    $ cd myproject
    $ python
    >>> import polls

If you got an ``ImportError``, it's just as it sounds!



.. _webapp_answers_pyc_files:

What are these .pyc files anyway?
----------------------------------

From `PEP 3147 <http://www.python.org/dev/peps/pep-3147/#background>`_:

    CPython (the 'standard' variety of Python) compiles its source code into "byte code", and for performance reasons, it caches this byte code on the file system whenever the source file has changes. This makes loading of Python modules much faster because the compilation phase can be bypassed. When your source file is ``foo.py``, CPython caches the byte code in a ``foo.pyc`` file right next to the source.

When you import or otherwise run a piece of Python code, it will create a .pyc file of the compiled byte code automatically when it can. 



.. _webapp_answers_why_only_restore_py_not_pyc:


Why do I only need to restore settings.py and not settings.pyc?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Well first off, remember how we set up git to exclude ``.pyc`` files from the repo? So ``settings.pyc`` was never put into the repo and therefore cannot be recovered from it. Not to worry though. When you restore ``settings.py`` and restart the dev server, ``settings.pyc`` is built automatically. Nifty!




