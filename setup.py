from setuptools import setup, find_packages
import sys, os

version = '0.1.2'

setup(name='collective.checkdocs',
      version=version,
      description="Distutils command to view and validate restructured text in package's long_description",
      long_description=open("README.txt").read(),
      classifiers=[
        "Programming Language :: Python",
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
      entry_points = {
         "distutils.commands": [
            "checkdocs = collective.checkdocs:checkdocs",
            "showdocs = collective.checkdocs:showdocs",
          ]
        }
      )
