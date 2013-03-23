# encoding: utf-8
# Copyright 2013 maker
# License
"""
Identities: Hardtree module definition
"""

PROPERTIES = {
              'title': 'Contacts',
              'details': 'Manage users, groups, companies and corresponding contacts',
              'url': '/contacts/',
              'system': True,
              'type': 'minor',
              }


URL_PATTERNS = [
                '^/contacts/',
                ]

#
# Cron
#

from maker.identities.cron import cron_integration

CRON = [cron_integration]
