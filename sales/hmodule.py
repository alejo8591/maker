# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Sales: maker module definition
"""

PROPERTIES = {
              'title': 'Sales & Stock',
              'details': 'Sales and Client Relationship Management',
              'url': '/sales/',
              'system': False,
              'type': 'major'
              }

URL_PATTERNS = [
                '^/sales/',
                ]

from maker.sales.cron import subscription_check

#Temporarily disabled cron due to failing .currency setting
#CRON = [subscription_check]
