# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Finance: Hardtree module definition
"""

PROPERTIES = {
              'title': 'Finance',
              'details': 'Manage finance',
              'url': '/finance/',
              'system': False,
              'type': 'minor',
              }


URL_PATTERNS = [
                '^/finance/',
                ]


from maker.finance.cron import assets_depreciate

CRON = [assets_depreciate]
