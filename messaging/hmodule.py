# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

"""
Messaging: Hardtree module definition
"""

PROPERTIES = {
              'title': 'Messaging',
              'details': 'Sending messages',
              'url': '/messaging/',
              'system': False,
              'type': 'minor',
              }

URL_PATTERNS = [
                '^/messaging/',
                ]


#
# Cron
#
from maker.messaging.cron import process_email

CRON = [process_email]
