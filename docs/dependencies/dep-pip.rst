

.. _dep-pip-label:

pip
--------------------

.. _dep-pip-what-label:

What is ``pip``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``pip`` is a utility for install and uninstalling Python packages. 
Packages are bundles of code that give additional functionality to an
existing Python installation.

.. _dep-pip-why-label:

Why do I need ``pip``?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install and manage packages in a consistent way in Python.

.. _dep-pip-how-label:

Get ``pip``!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, install ``ez_setup`` to get ``easy_install`` (the *old* python
package managers).  

#.  Download and save: http://peak.telecommunity.com/dist/ez_setup.py
#.  Open a terminal, and navigate to where it is downloaded.  
#.  Install::

        python ez_setup.py
        easy_install pip
        pip install virtualenv
        
        # or if those don't work!
        
        sudo python ez_setup.py
        sudo easy_install pip
        sudo pip install virtualenv


.. _pip-verify-label:


Verify It Works!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After it installs, run ``pip`` .   You should see something like::

    $ pip
    Usage: pip COMMAND [OPTIONS]

    pip: error: You must give a command (use "pip help" to see a list of commands)
