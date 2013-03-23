# encoding: utf-8
# Copyright 2013 maker
# License

"""
	Cron Job for Messaging module
"""
from maker.messaging.models import MessageStream

def process_email():
    "Process email"
    streams = MessageStream.objects.filter(trash=False, incoming_server_username__isnull=False)
    
    for stream in streams:
        stream.process_email()
