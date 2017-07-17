# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='contacts')
    name = models.CharField(max_length=200, unique=True)
    phone_numbers = models.ManyToManyField('app.PhoneNumber')

    def __unicode__(self):
        return self.name


class PhoneNumber(models.Model):

    # https://github.com/stefanfoulis/django-phonenumber-field
    number = PhoneNumberField()

    def __unicode__(self):
        return self.number
