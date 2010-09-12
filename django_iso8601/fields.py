# -*- coding: utf8 -*-

from datetime import date, datetime, time

import isodate

from django import forms
from django.utils.translation import ugettext_lazy as _

from django_iso8601.widgets import ISO8601DateInput, ISO8601DatetimeInput, ISO8601TimeInput


__all__ = 'ISO8601DateField', 'ISO8601DatetimeField', 'ISO8601TimeField'


class ISO8601DateField(forms.Field):
    widget = ISO8601DateInput
    default_error_messages = {
        'invalid': _(u'Enter a valid ISO 8601 date.'),
    }

    def __init__(self, yeardigits=4, **kwargs):
        self.yeardigits = yeardigits
        super(ISO8601DateField, self).__init__(**kwargs)

    def to_python(self, value):
        """
        Validates that the input can be converted to a date. Returns a Python
        datetime.date object.
        """
        if value in forms.fields.EMPTY_VALUES:
            return None
        if isinstance(value, date):
            return value
        try:
            return isodate.parse_date(value, yeardigits=self.yeardigits)
        except (isodate.ISO8601Error, ValueError, TypeError):
            raise forms.ValidationError(self.error_messages['invalid'])


class ISO8601DatetimeField(forms.Field):
    widget = ISO8601DatetimeInput
    default_error_messages = {
        'invalid': _(u'Enter a valid ISO 8601 datetime.'),
    }

    def to_python(self, value):
        """
        Validates that the input can be converted to a datetime. Returns a Python
        datetime.datetime object.
        """
        if value in forms.fields.EMPTY_VALUES:
            return None
        if isinstance(value, datetime):
            return value
        try:
            return isodate.parse_datetime(value)
        except (isodate.ISO8601Error, ValueError, TypeError):
            raise forms.ValidationError(self.error_messages['invalid'])


class ISO8601TimeField(forms.Field):
    widget = ISO8601TimeInput
    default_error_messages = {
        'invalid': _(u'Enter a valid ISO 8601 time.'),
    }

    def to_python(self, value):
        """
        Validates that the input can be converted to a time. Returns a Python
        time.time object.
        """
        if value in forms.fields.EMPTY_VALUES:
            return None
        if isinstance(value, time):
            return value
        try:
            return isodate.parse_time(value)
        except (isodate.ISO8601Error, ValueError, TypeError):
            raise forms.ValidationError(self.error_messages['invalid'])

