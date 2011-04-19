In the Beginning was the Command Line Badge
===========================================

In the Beginning was the Command Line is a book by Neal Stephenson. Unlike many of his other works, it is short and available for free (legal, even) download on the internet. The first part of this badge is to do just that; the second part of the badge is to read the section entitled "THE HOLE HAWG OF OPERATING SYSTEMS."

If you just want to read the book already, [:ref:`skip to the end  <the_end>`]. Otherwise we will complete this badge the UNIX way:

.. code-block:: bash

   $ curl 'http://www.cryptonomicon.com/command.zip' | gunzip | grep -A 22 "THE HOLE HAWG OF OPERATING SYSTEMS"

Read the text that is on your screen the come back here for the breakdown on the command you just read.

Let's look at this in chunks. The first chunk is the ``curl`` command. ``curl`` is a standard UNIX tool that transfers data to or from a server. You likely used ``curl`` to download ``pip`` during the setup. In essence, we are fetching the zip file hosted at www.cryptonomicon.com that contains a compressed version of the text. If you just run ``curl 'http://www.cryptonomicon.com/command.zip'`` you will see the contents of the zip file found at that url printed to standard out (aka, your screen). Not very interesting.

(In fact, your screen will be filled with junk. Get rid of it by running ``clear``.)

To make it interesting, we need to unzip it. The "it" here is what ``curl`` prints to standard out, which is the zip file. In UNIX, you can redirect the output of one command to the input of another using a handy character called "pipe" which looks like this: ``|``. In plain English, we will "pipe" the output of the ``curl`` comand into the UNIX unzip tool, which is called ``gunzip``. If you just run ``curl 'http://www.cryptonomicon.com/command.zip' | gunzip`` you will see the entire contents of the file contained in the zip file printed to your screen.

Finally, we want to print to standard out just the section we want to read. To identify the "THE HOLE HAWG OF OPERATING SYSTEMS," we will us a UNIX tool called ``grep``, which finds text that matches a string you give it. In this case, we give it the string "THE HOLE HAWG OF OPERATING SYSTEMS" - the title of the section. The ``-A`` optional argument allows you to specify how many lines of text after the matched text ``grep`` should print to the screen. Here we tell ``grep`` to print 22 lines because that is how long the section of text is. 

That's it.

In short, we want to grab the zip file from the url using ``curl``, pipe it to ``gunzip`` to extract the actual text and pipe that to ``grep`` to print to standard out the section of interest. And all without actually downloading the file to your computer!
 
Even shorter, UNIX is awesome!


To download the whole text to your computer so you can read more, using the CLI::
    
    $ curl 'http://www.cryptonomicon.com/command.zip' | gunzip > command.txt


.. _the_end:

If you need a break from the CLI, download the book using this link: http://www.cryptonomicon.com/command.zip. 
