# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contact, PhoneNumber


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    model = PhoneNumber
