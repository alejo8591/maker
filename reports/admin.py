# encoding: utf-8
# Copyright 2013 maker
# License
"""
	Reports module: Admin page
"""
from maker.reports.models import Report
from django.contrib import admin  
    
class ReportAdmin(admin.ModelAdmin):
    """ 
    	Message stream admin 
    """
    list_display = ('name', 'model', 'content')
    search_fields = ['name']
    
admin.site.register(Report, ReportAdmin)
