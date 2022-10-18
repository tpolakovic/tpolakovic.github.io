#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tomas Polakovic'
SITENAME = 'A Bit Correlated'
SITEURL = 'https://tpolakovic.github.io'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Art Portfolio', 'https://tompolakovic.crevado.com'),
    ('Scholarly Portfolio', 'https://scholar.google.com/citations?user=ElHnfB8AAAAJ'),
)

# Social widget
SOCIAL = (
    ('github-square', 'https://github.com/tpolakovic'),
    ('twitter-square', 'https://twitter.com/TomPolakovic'),
    ('reddit-square', 'https://www.reddit.com/user/tpolakov1/'),
)

DEFAULT_PAGINATION = 10

MARKUP = ('md', 'pelican-ipynb')

PLUGIN_PATHS = ['./pelican-plugins']
STATIC_PATHS = ['img']
PLUGINS = ['ipynb.markup']
IGNORE_FILES = [".ipynb_checkpoints"]

THEME = './themes/Flex'
FAVICON = '/img/favicon.ico'
SITELOGO = 'https://i.imgur.com/1tK0x4P.jpg?2'
SITETITLE = SITENAME
SITESUBTITLE = 'Physics and stuff...'
MAIN_MENU = True
COPYRIGHT_YEAR = 2019
COPYRIGHT_NAME = 'Tomas Polakovic'
BROWSER_COLOR = '#333333'
MENUITEMS = (
    ('Archive', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)
ROBOTS = 'index, follow'
