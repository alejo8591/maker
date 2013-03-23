# encoding: utf-8
# Copyright 2013 maker
# License

from django import forms


class AuthorizeRequestTokenForm(forms.Form):
    oauth_token = forms.CharField(widget=forms.HiddenInput)
    authorize_access = forms.BooleanField(required=True)
