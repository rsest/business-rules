#! /usr/bin/env python

import setuptools

from business_rules import __version__ as version

with open('HISTORY.rst') as f:
    history = f.read()

description = 'Python DSL for setting up business intelligence rules that can be configured without code; based on Venmo/business-rules.'

setuptools.setup(
        name='business-rules-engine',
        version=version,
        description='{0}'.format(description),
        author='Rodrigo Sestari',
        url='https://github.com/rodrigosestari/business-rules',
        packages=['business_rules'],
        license='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
        ],
)