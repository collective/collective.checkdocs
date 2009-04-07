"""
        
        Provide checkdocs and showdocs commands for distutils.

        Use docutils to do reST -> HTML translation. Hook into docutils via monkey-patching to get the error status out of it.

"""

__author__ = "Mikko Ohtamaa <mikko.ohtamaa@twinapex.com>"
__license__ = "GPL"
__copyright__ = "Twinapex Research"

import os
import sys
import webbrowser
from random import random
from cStringIO import StringIO
import BaseHTTPServer
import SimpleHTTPServer

from docutils.core import publish_parts

from distutils.errors import *
from distutils import log
from setuptools.command.setopt import edit_config, option_base, config_file

def rst2html(value):
    """ Run rst2html translation """
    docutils_settings = {}
    parts = publish_parts(source=value,
            writer_name="html4css1",
            settings_overrides=docutils_settings)
    return parts['whole']

def do_GET(self):
    """ Dummy web server which serves translated reST document """
    f = StringIO()
    self.send_response(200)
    print >> f, self.value.encode('utf-8')
    self.send_header('Content-Type','text/html;charset=utf-8')
    self.end_headers()
    f.seek(0)
    self.copyfile(f, self.wfile)
    f.close()
    return

SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET = do_GET


# This global holds errors/warnings spit out by docutils
reports = []

#
# Monkey patch crap out of docutils
#

from docutils import utils

orignal_system_message = utils.Reporter.system_message

def system_message(self, level, message, *children, **kwargs):
    result = orignal_system_message(self, level, message, *children, **kwargs)
    if level >= self.WARNING_LEVEL:
        # All reST failures preventing doc publishing go to reports 
        # and thus will result to failed checkdocs run
        reports.append(message)
 
    return result


class checkdocs(option_base):

    description = "validate long_description restructured text and print warnings and errors to standard output"

    user_options = [
        ]
    boolean_options = []

    def initialize_options(self):
        option_base.initialize_options(self)

    def finalize_options(self):
        option_base.finalize_options(self)

    def run(self):
        text = self.distribution.get_long_description()
        docutils_settings = {}

        # Monkeypatch docutils for simple error/warning output support
        utils.Reporter.system_message = system_message

        html = rst2html(text)

        # Unmonkey
        utils.Reporter.system_message = orignal_system_message

        if len(reports) > 0:
            raise CompileError("long_description had reST syntax errors")

class showdocs(option_base):
    """ Inspired by http://pypi.python.org/pypi/rstctl """
    description = "Open the documentation in local web browser, converted to HTML"

    user_options = [
        ]
    boolean_options = []

    def initialize_options(self):
        option_base.initialize_options(self)

    def finalize_options(self):
        option_base.finalize_options(self)

    def run(self):
        handler=SimpleHTTPServer.SimpleHTTPRequestHandler
        handler.value = rst2html(self.distribution.get_long_description())
        httpd = BaseHTTPServer.HTTPServer(('',6969), handler)
        webbrowser.open('http://localhost:6969/%s' % random())
        print 'reST to HTML conversion available at at http://localhost:6969/ - press CTRL+C to interrupt'
        try:
            httpd.handle_request()
        except KeyboardInterrupt:
            return
                
__all__ = ('checkdocs','showdocs')
