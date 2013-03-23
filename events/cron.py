# encoding: utf-8
# Copyright 2013 maker
# License


"""
	Events Cron jobs
"""

from maker.events import integration

def cron_integration():
    "Run integration"
    try:
        integration.sync()
    except Exception:
        pass

