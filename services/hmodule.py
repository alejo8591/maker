# encoding: utf-8
# Copyright 2013 maker
# License

"""
Service Support: maker module definition
"""

PROPERTIES = {
              'title': 'Service Support',
              'details': 'Service delivery and support management',
              'url': '/services/',
              'system': False,
              'type': 'major'
              }

URL_PATTERNS = [
                '^/services/',
                ]

# Cron
from maker.services.cron import tickets_escalate

CRON = [tickets_escalate]
