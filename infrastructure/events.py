# encoding: utf-8
# Copyright 2013 maker
# License

"""
    Infrastructure integration with Events module
    Provides ItemServicing as EventRenderer instances
"""

from maker.infrastructure.models import ItemServicing
from maker.core.models import Object
from maker.events.rendering import EventRenderer
from django.db.models import Q
import datetime

def get_events(request):
    "Return a list of EventRenderers from available ItemServicing"
    events = []
    
    query = Q(expiry_date__isnull=False)
    service_records = Object.filter_by_request(request, manager=ItemServicing.objects.filter(query))
    for record in service_records:
        if record.expiry_date:
            old = record.expiry_date
            new_expiry_date = datetime.datetime(year=old.year, month=old.month, day=old.day, hour=12, minute=0, second=0)
            event = EventRenderer(record.name, None, new_expiry_date, record.get_absolute_url())
        event.css_class += " infrastructure-calendar-servicing"
        events.append(event)
        
    return events
