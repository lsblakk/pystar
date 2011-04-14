Command Line Module
===================

To earn the the Command Line Badge, you must be able to demostrate how to use the following commands at the command line (here after referred to as ``cmd``):

* cd
* pwd
* ls
* mkdir
* rm
* less
* man
* apropos
* which

You will also need to be familiar with the following concepts:

* directory paths
* arguments
* getting help

Goals:

* navigate (relative/absolute) using the commandline
* create and destroy directory structures
* call a program with arguments
* less a file
* learn to self rescue 

Exercise
---------

Open a command propt.
Type ``pwd`` (print working directory). Where are you?
Type ``ls`` (list). What do you see?
Create a directory: ``$ mkdir mydir``
Type ``ls`` again. What's different?
Change directories to ``mydir``: ``$ cd mydir``.
``ls``. What do you see?
Create a file called ``foo`` containing some text: ``$ echo "your text" > foo``
``ls``
View the contents of ``foo``: ``$ less foo`` (press 'q' to get out of the file)


cd
---

``cd`` stands for "change directory."

What arguments, if any, does ``cd`` take?

Try typing just ``cd`` into your cmd. What happens?


pwd
----

``pwd`` stands for "print working directory"

What arguments, if any, does ``pwd`` take?

ls
---

``ls`` stands for "list."

What arguments, if any, does ``ls`` take?

mkdir
------

``mkdir`` stands for "make directory."

What arguments, if any, does ``mkdir`` take?

rm
--

``rm`` stands for "remove"

What arguments, if any, does ``rm`` take?

less
----

``less`` is a program that allows you to view the contents of a file in your bash environment. There are a bunch of
different ways to view a file in the cmd (eg ``cat``, ``top``, ``more``) but ``less`` is nice because it allows you to move backwards and forwards through the contents and search the contents (among other things).

Try typing only ``less`` into your cmd. What happens? Why?
Give ``less`` an appropriate argument. What happens now? Where did your prompt go and how do you get it back?

man
---

``man`` is short for "manual" - instructions about how to use a particular command. The output of running the ``man``
command is called a "man page" or "manual page." Man pages open in ``less`` (see above).

What arguments, if any, does ``man`` take?

(Try typing ``man man`` into your cmd.)
