# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Sales Cron jobs
"""
from maker.sales.models import Subscription

def subscription_check(): 
    "Automatically depreciate assets as per their depreciation rate"
    
    subscriptions = Subscription.objects.all()
    for subscription in subscriptions:
        subscription.check_status()
