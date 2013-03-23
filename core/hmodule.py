# encoding: utf-8
# Copyright 2013 maker
# License

"""
Core: maker module definition
"""

PROPERTIES = {
              'title': 'Administration',
              'details': 'Core Administration',
              'url': '/admin/',
              'system': True,
              'type': 'user',
              }

URL_PATTERNS = [
                '^/admin/',
                ]

from maker.core.cron import email_reply
#CRON = [email_reply, ]
CRON = []
