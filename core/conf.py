# encoding: utf-8
# Copyright 2013 maker
# License


"""
	Multitenancy settings
"""
from django.conf import LazySettings
from pandora import box


class Settings(LazySettings):
	""" 
		A lazy proxy for either global Django settings or a custom settings object.
		The user can manually configure settings prior to using them. Otherwise,
		Django uses the settings module pointed to by DJANGO_SETTINGS_MODULE. 
	"""
	def __getattr__(self, key):
		if key in box:
			return box[key]
		else:
			return super(Settings, self).__getattr__(key)

settings = Settings()