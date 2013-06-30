from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='two.bootstrap',
      version=version,
      description="bootstrap templates for two",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Ivo van der Wijk',
      author_email='two@in.m3r.nl',
      url='http://github.com/iivvoo/two.bootstrap',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['two', 'two.bootstrap'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'two.ol'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

