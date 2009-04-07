collective.checkdocs
====================

collective.checkdocs adds new distutils commands ``checkdocs`` and ``showdocs`` to validate restructured text in long_description field of Python eggs. 
This package aims to make Python egg help page publishing and editing easier.

Eggs' long description field, which is usually also the README.txt file of the package, is reST formatted text. This text is converted
to HTML to show on the package page when package is published in distribution repositories like PyPI or plone.org.
Unfortunately, since repositories do poor job to validate incoming reST text, errors in the text will result to broken published
package pages. 

Unpublishing is usually very cumbersome. We save our time by validating reST input using ``checkdocs`` and ``showdocs`` commands.

New commands
============

The following commands will be added to all setup.py installers.

checkdocs
---------

Run long_description through reST to HTML converter and print errors and warnings to the standard output.

Any errors and warnings will cause distutils to abort.

Example::

  python setup.py checkdocs
  <string>:4: (WARNING/2) Inline literal start-string without end-string.
  error: long_description had reST syntax errors

showdocs
---------

Run long_description through reST to HTML converter and display the result in a local webbrowser. Runs a web server in port 6969 until CTRL+C is pressed.

Example::

  python setup.py showdocs
  running showdocs
  reST to HTML conversion available at at http://localhost:6969/ - press CTRL+C to interrupt


Resources
---------

* long_description text is `restructured formatted <http://docutils.sourceforge.net/rst.html>`_

* `docutils <http://docutils.sourceforge.net/>`_

* `rstctl (inspiration and sources) <http://pypi.python.org/pypi/rstctl>`_
