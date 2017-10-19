# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label=False, widget=forms.TextInput(attrs={'id': 'post-text', 'required': True,'class': 'contact-write__input','placeholder': 'Имя'}))
    sender = forms.EmailField(label=False ,widget=forms.TextInput(attrs={'class': 'contact-write__input','placeholder': 'Почта'}))
    message_mail = forms.CharField(label=False, widget=forms.Textarea(attrs={'class': 'contact-write__textarea','placeholder': 'Почта'}))
    #copy = forms.BooleanField(required=False)

    #widget = forms.TextInput(attrs={'placeholder': 'Search'}))