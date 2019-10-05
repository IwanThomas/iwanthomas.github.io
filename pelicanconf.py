#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Iwan Thomas'
SITENAME = "Iwan's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Iwan Edits 
# set theme
THEME = "pelican-themes/blue-penguin"

# Enable jupyter notebook blog posts
MARKUP = ('md', 'ipynb')

# PLUGIN_PATHS = ['./plugins']
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['ipynb.markup']
# PLUGIN_PATHS = ['./pelican-plugins']
# PLUGINS = ['pelican-ipynb.markup']


# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]  

# Iwan Edits Over

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True