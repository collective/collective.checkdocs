from distutils.core import PyPIRCCommand
from distutils.errors import *
from distutils import log

class checkdocs(PyPIRCCommand):

    description = "validate long_description restructured text and print warnings and errors to standard output"

    user_options = [
        ]
    boolean_options = []

    def initialize_options(self):
        PyPIRCCommand.initialize_options(self)

    def finalize_options(self):
        PyPIRCCommand.finalize_options(self)

    def run(self):
        pass

