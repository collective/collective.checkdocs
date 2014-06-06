from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='collective.checkdocs',
      version=version,
      description="Distutils command to view and validate restructured text in package's long_description",
      long_description=open("README.txt").read(),
      classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='rest distutils egg validator check validation restructured text html documentation',
      author='mFabrik Research Oy',
      author_email='info@mfabrik.com',
      url='http://pypi.python.org/pypi/collective.checkdocs',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,        
      namespace_packages=["collective"],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          "docutils"
      ],
      test_suite='collective.checkdocs.tests',
      entry_points = {
         "distutils.commands": [
            "checkdocs = collective.checkdocs:checkdocs",
            "showdocs = collective.checkdocs:showdocs",
          ]
        }
      )
