#!/usr/bin/env python

from distutils.core import setup

setup(name='Auto-WAB-Mailer',
      version='1.0',
      description='Send WAB Emails Daily!',
      author='Daniel McKeon',
      author_email='dftm@wharton.upenn.edu',
      url='https://www.dftmckeon.com/',
      install_requires=['praw', 'pyowm', 'email.mime.multipart', 'email.mime.text', 'time', 'random']
     )
