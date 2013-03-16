# encoding: utf-8
# Copyright 2011 Tree.io Limited
# This file is part of maker.
# License www.tree.io/license

"""
Sales Cron jobs
"""
from maker.sales.models import Subscription

def subscription_check(): 
    "Automatically depreciate assets as per their depreciation rate"
    
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.check_status()
