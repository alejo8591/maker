

# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Account: maker module definition
"""

PROPERTIES = {
              'title': 'Account',
              'details': 'User Account',
              'url': '/account/',
              'system': True,
              'type': 'user',
              }

URL_PATTERNS = [
                '^/account/',
                ]

#
# Cron
#
from maker.account.cron import CronNotifier
cron_notifier = CronNotifier()

CRON = [cron_notifier.send_notifications]
