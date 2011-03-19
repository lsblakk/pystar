.. _linux-setup-label:

====================
Linux Setup Guide
====================

TextEditor
--------------
Most Linux distros come with a text editor like gedit which will
be enough for this workshop, however if you have a text editor
you prefer to work in, please do. To start GEdit: click Applications, 
point to Accessories, and click Text Editor or you can start it 
from a terminal with:

.. code-block:: bash

    gedit

Python
---------------

Linux ships with Python installed, so the goal of this page is to
make sure you can start a terminal and run Python from the 
command line. 

Start up a terminal. You can find the Terminal application at 
Applications/Accessories/Terminal, or it may already be on 
your menu bar. Test your Python install at the command prompt:

.. code-block:: bash

    python
 
    # output should look something like
    Python 2.5.2 (r252:60911, Jan 24 2010, 17:44:40) 
    [GCC 4.3.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information
    >>>

To exit the Python prompt, type:

.. code-block:: bash
    
    exit()

This will take you back to the Terminal command prompt.

Virtualenv
----------------
You'll need the virtualenv package.

For Fedora/Red Hat/CentOS based environments:

.. code-block:: bash

    sudo yum -y install python-virtualenv gcc openssl-devel
    sudo yum-builddep -y python-lxml pyOpenSSL python-sqlite2

On Ubuntu/Debian:

.. code-block:: bash

    sudo apt-get install git python-dev python-virtualenv

Tkinter: Color Wall
----------------------------

The ColorWall project depends on Tkinter which is 
pre-installed on some Linux* distributions. To check 
if you have Tkinter installed, open your Terminal 
window and start your Python prompt:

.. code-block:: python

    >>> import Tkinter

If that command results in an ImportError try following instructions 
for `installing Tkinter <http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter>`_ 
and if you have problems let an instructor/helper know and they'll help you.

(On some Debian installation, when you import Tkinter
it will tell you that you need to install the python-tk package, 
which you should do). After you are done at the Python prompt, 
exit to the regular terminal by typing exit() and hitting enter. 


Django: Web App
--------------------------
** coming soon


Git: Web App
---------------
** coming soon


Web Accounts
-----------------
Please go set up accounts with the following services to use during the workshop.

- `Alwaysdata <http://alwaysdata.com/>`_ (free django hosting/deployment)

    - Click Sign up now
    - Choose the "Pack gratuit (10 Mo)". It means "Free account (10 megabytes of storage)".
    - Choose the monthly payment plan. 

- `Github <http://github.com/>`_ (free git repository hosting/sharing)

    - For now just create an account, with any username you want, we'll come back to setting up a repo/ssh key
    
