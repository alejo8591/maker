# encoding: utf-8
# Copyright 2013 maker
# License


"""
	Events: maker module definition
"""

PROPERTIES = {
              'title': 'Calendar',
              'details': 'Manage events and calendars',
              'url': '/calendar/',
              'system': True,
              'type': 'minor',
              }


URL_PATTERNS = [
                '^/calendar/',
                ]

# Cron
from maker.events.cron import cron_integration

CRON = [cron_integration]
