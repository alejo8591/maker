# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

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
