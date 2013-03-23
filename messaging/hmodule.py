# encoding: utf-8
# Copyright 2013 maker
# License

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
