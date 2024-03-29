# encoding: utf-8
# Copyright 2013 maker
# License

"""
    Finance integration with Events module
    Provides Liabilities as EventRenderer instances
"""

from maker.finance.models import Liability
from maker.core.models import Object
from maker.events.rendering import EventRenderer
from django.db.models import Q
import datetime

def get_events(request):
    "Return a list of EventRenderers from available Liability"
    events = []
    
    
    
    query = Q(due_date__isnull=False)
    liabilities = Object.filter_by_request(request, manager=Liability.objects.filter(query))
    for liability in liabilities:
        if liability.due_date:
            old = liability.due_date
            new_due_date = datetime.datetime(year=old.year, month=old.month, day=old.day, hour=12, minute=0, second=0)
            event = EventRenderer(liability.name, None, new_due_date, liability.get_absolute_url())
        event.css_class += " finance-calendar-liability"
        events.append(event)
        
    return events
