.. _coiorwall-label:

=============
Intro to Programming Python: Color Wall
=============

The ColorWall is a framework for implementing and displaying effects for a wall of pixels. 
During this workshop, you will write your own ColorWall and design effects for it.

You can also see the ColorWall in action here: http://vimeo.com/16522975.

Layout
--------

The ColorWall code consists of 3 files:

- run.py -- takes arguments from your environment (like a specified width and height for the wall), set up the wall and effects, and run them.
- wall.py -- the logic behind the matrix of squares that make up the wall. This file has a comment block at the top that summarize the interface that you will use when programming your own effects.
- effects.py -- where effects live. This is the main file that you'll be editing during the workshop.

Resources
-----------

- http://openhatch.org/wiki/Boston_Python_workshop/Friday_handout#Setting_up_the_ColorWall
- https://github.com/jesstess/ColorWall ColorWall code on GitHub
- The ColorWall uses the HSV color space. Wikipedia has a http://en.wikipedia.org/wiki/HSL_and_HSV complicated explanation for what that means, but what it boils down to for the purposes of our project is this: each pixel gets 3 values: hue (e.g. am I red, green, or blue), saturation (am I pale or intense), and value (am I bright or dark). <code>effects.py</code> has example effects that exercise hue, saturation, and value independently.
