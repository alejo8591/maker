# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Identities Cron jobs
"""

from maker.identities import integration

def cron_integration():
    "Run integration"
    try:
        integration.sync()
    except:
        pass
