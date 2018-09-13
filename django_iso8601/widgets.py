# -*- coding: utf8 -*-

from datetime import date, datetime, time

import isodate

from django.forms.widgets import Input

__all__ = 'ISO8601DateInput', 'ISO8601DatetimeInput', 'ISO8601TimeInput'


class ISO8601DateInput(Input):
    input_type = 'text'

    def __init__(self, attrs=None, format="%Y-%m-%d", yeardigits=4):
        super(ISO8601DateInput, self).__init__(attrs)
        self.format = format
        self.yeardigits = yeardigits

    def format_value(self, value):
        if isinstance(value, date):
            return isodate.date_isoformat(value, self.format, self.yeardigits)
        return value


class ISO8601DatetimeInput(Input):
    input_type = 'text'

    def __init__(self, attrs=None, format="%Y-%m-%dT%H:%M:%S%Z"):
        super(ISO8601DatetimeInput, self).__init__(attrs)
        self.format = format

    def format_value(self, value):
        if isinstance(value, datetime):
            return isodate.datetime_isoformat(value, self.format)
        return value


class ISO8601TimeInput(Input):
    input_type = 'text'

    def __init__(self, attrs=None, format="%H:%M:%S%Z"):
        super(ISO8601TimeInput, self).__init__(attrs)
        self.format = format

    def format_value(self, value):
        if isinstance(value, time):
            try:
                return isodate.time_isoformat(value, self.format)
            except:
                return repr(value)
        return value

