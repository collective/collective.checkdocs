import unittest
import setuptools
from distutils.dist import Distribution
from distutils.errors import CompileError
from collective.checkdocs import checkdocs, reports
import sys
import StringIO

class CheckDocTest(unittest.TestCase):
    
    def setUp(self):
        # Silence the docutils errors
        self.stderr = sys.stderr
        sys.stderr = StringIO.StringIO()
        
    def tearDown(self):
        sys.stderr = self.stderr
        # Get rid of any lingering errors:
        while reports:
            reports.pop()
        
    def test_succeeds(self):
        dist = Distribution(attrs={'long_description': 'This works\n==========\n\n'})
        command = checkdocs(dist)
        command.initialize_options()
        command.finalize_options()
        checkdocs(dist).run()
        
    def test_fails(self):
        dist = Distribution(attrs={'long_description': 'This do no work\n========\n**'})
        command = checkdocs(dist)
        command.initialize_options()
        command.finalize_options()
        self.assertRaises(CompileError, command.run)

test_suite = unittest.makeSuite(CheckDocTest)