# encoding: utf-8
# Copyright 2013 maker
# License

# Django imports
import django.dispatch 

# Piston imports
from utils import send_consumer_mail

def consumer_post_save(sender, instance, created, **kwargs):
    pass

def consumer_post_delete(sender, instance, **kwargs):
    instance.status = 'canceled'
    pass

