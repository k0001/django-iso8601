# -*- coding: utf8 -*-

#  Most of the test cases here are from isodate package from:
#   - Homepage: http://cheeseshop.python.org/pypi/isodate
#   - Author: Gerhard Weis <gerhard weis at proclos com>
#   - License: BSD

import os
import unittest
from datetime import date, datetime, time

from isodate import parse_date, ISO8601Error, date_isoformat, FixedOffset, UTC, \
    DATE_CENTURY, DATE_YEAR, DATE_MONTH, DATE_EXT_COMPLETE, DATE_BAS_COMPLETE, \
    DATE_BAS_ORD_COMPLETE, DATE_EXT_ORD_COMPLETE, DATE_BAS_WEEK, \
    DATE_BAS_WEEK_COMPLETE, DATE_EXT_WEEK, DATE_EXT_WEEK_COMPLETE, \
    TIME_BAS_MINUTE, TZ_BAS, TIME_EXT_MINUTE, TZ_EXT, TZ_HOUR, \
    TIME_BAS_COMPLETE, TIME_EXT_COMPLETE, TIME_HOUR


DATE_Y4_TEST_CASES = [
    ('19', date(1901, 1, 1), DATE_CENTURY),
    ('1985', date(1985, 1, 1), DATE_YEAR),
    ('1985-04', date(1985, 4, 1), DATE_MONTH),
    ('1985-04-12', date(1985, 4, 12), DATE_EXT_COMPLETE),
    ('19850412', date(1985, 4, 12), DATE_BAS_COMPLETE),
    ('1985102', date(1985, 4, 12), DATE_BAS_ORD_COMPLETE),
    ('1985-102', date(1985, 4, 12), DATE_EXT_ORD_COMPLETE),
    ('1985W155', date(1985, 4, 12), DATE_BAS_WEEK_COMPLETE),
    ('1985-W15-5', date(1985, 4, 12), DATE_EXT_WEEK_COMPLETE),
    ('1985W15', date(1985, 4, 8), DATE_BAS_WEEK),
    ('1985-W15', date(1985, 4, 8), DATE_EXT_WEEK),
    ('1989-W15', date(1989, 4, 10), DATE_EXT_WEEK),
    ('1989-W15-5', date(1989, 4, 14), DATE_EXT_WEEK_COMPLETE),
    ('1-W1-1', None, DATE_BAS_WEEK_COMPLETE)]

DATE_Y6_TEST_CASES = [
    ('+0019', date(1901, 1, 1), DATE_CENTURY),
    ('+001985', date(1985, 1, 1), DATE_YEAR),
    ('+001985-04', date(1985, 4, 1), DATE_MONTH),
    ('+001985-04-12', date(1985, 4, 12), DATE_EXT_COMPLETE),
    ('+0019850412', date(1985, 4, 12), DATE_BAS_COMPLETE),
    ('+001985102', date(1985, 4, 12), DATE_BAS_ORD_COMPLETE),
    ('+001985-102', date(1985, 4, 12), DATE_EXT_ORD_COMPLETE),
    ('+001985W155', date(1985, 4, 12), DATE_BAS_WEEK_COMPLETE),
    ('+001985-W15-5', date(1985, 4, 12), DATE_EXT_WEEK_COMPLETE),
    ('+001985W15', date(1985, 4, 8), DATE_BAS_WEEK),
    ('+001985-W15', date(1985, 4, 8), DATE_EXT_WEEK)]

DATETIME_TEST_CASES = [
    ('19850412T1015', datetime(1985, 4, 12, 10, 15),
     DATE_BAS_COMPLETE + 'T' + TIME_BAS_MINUTE),
    ('1985-04-12T10:15', datetime(1985, 4, 12, 10, 15),
     DATE_EXT_COMPLETE + 'T' + TIME_EXT_MINUTE),
    ('1985102T1015Z', datetime(1985, 4, 12, 10, 15, tzinfo=UTC),
     DATE_BAS_ORD_COMPLETE + 'T' + TIME_BAS_MINUTE + TZ_BAS),
    ('1985-102T10:15Z', datetime(1985, 4, 12, 10, 15, tzinfo=UTC),
     DATE_EXT_ORD_COMPLETE + 'T' + TIME_EXT_MINUTE + TZ_EXT),
    ('1985W155T1015+0400', datetime(1985, 4, 12, 10, 15, tzinfo=FixedOffset(4, 0, '+0400')),
     DATE_BAS_WEEK_COMPLETE + 'T' + TIME_BAS_MINUTE + TZ_BAS),
    ('1985-W15-5T10:15+04', datetime(1985, 4, 12, 10, 15, tzinfo=FixedOffset(4, 0, '+0400')),
     DATE_EXT_WEEK_COMPLETE + 'T' + TIME_EXT_MINUTE + TZ_HOUR)]

TIME_TEST_CASES = [
    ('232050', time(23, 20, 50), TIME_BAS_COMPLETE + TZ_BAS),
    ('23:20:50', time(23, 20, 50), TIME_EXT_COMPLETE + TZ_EXT),
    ('2320', time(23, 20), TIME_BAS_MINUTE),
    ('23:20', time(23, 20), TIME_EXT_MINUTE),
    ('23', time(23), TIME_HOUR),
    ('232050,5', time(23, 20, 50, 500000), None),
    ('23:20:50.5', time(23, 20, 50, 500000), None),
    ('2320,8', time(23, 20, 48), None),
    ('23:20,8', time(23, 20, 48), None),
    ('23,3', time(23, 18), None),
    ('232030Z', time(23, 20, 30, tzinfo=UTC), TIME_BAS_COMPLETE + TZ_BAS),
    ('2320Z', time(23, 20, tzinfo=UTC), TIME_BAS_MINUTE + TZ_BAS),
    ('23Z', time(23, tzinfo=UTC), TIME_HOUR + TZ_BAS),
    ('23:20:30Z', time(23, 20, 30, tzinfo=UTC), TIME_EXT_COMPLETE + TZ_EXT),
    ('23:20Z', time(23, 20, tzinfo=UTC), TIME_EXT_MINUTE + TZ_EXT),
    ('152746+0100', time(15, 27, 46, tzinfo=FixedOffset(1, 0, '+0100')), TIME_BAS_COMPLETE + TZ_BAS),
    ('152746-0500', time(15, 27, 46, tzinfo=FixedOffset(-5, 0, '-0500')), TIME_BAS_COMPLETE + TZ_BAS),
    ('152746+01', time(15, 27, 46, tzinfo=FixedOffset(1, 0, '+01:00')), TIME_BAS_COMPLETE + TZ_HOUR),
    ('152746-05', time(15, 27, 46, tzinfo=FixedOffset(-5, -0, '-05:00')), TIME_BAS_COMPLETE + TZ_HOUR),
    ('15:27:46+01:00', time(15, 27, 46, tzinfo=FixedOffset(1, 0, '+01:00')), TIME_EXT_COMPLETE + TZ_EXT),
    ('15:27:46-05:00', time(15, 27, 46, tzinfo=FixedOffset(-5, -0, '-05:00')), TIME_EXT_COMPLETE + TZ_EXT),
    ('15:27:46+01', time(15, 27, 46, tzinfo=FixedOffset(1, 0, '+01:00')), TIME_EXT_COMPLETE + TZ_HOUR),
    ('15:27:46-05', time(15, 27, 46, tzinfo=FixedOffset(-5, -0, '-05:00')), TIME_EXT_COMPLETE + TZ_HOUR),
    ('1:17:30', None, TIME_EXT_COMPLETE)]



class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self._old_settings_mod = os.environ.get('DJANGO_SETTINGS_MODULE', None)
        os.environ['DJANGO_SETTINGS_MODULE'] = 'django_iso8601' # whatever

    def tearDown(self):
        if self._old_settings_mod is not None:
            os.environ['DJANGO_SETTINGS_MODULE'] = self._old_settings_mod



def create_date_testcase(yeardigits, datestring, expectation, format):

    class TestDate(BaseTestCase):

        def test_field(self):
            from django_iso8601 import ISO8601DateField
            from django.forms import ValidationError

            field = ISO8601DateField(yeardigits=yeardigits)

            if expectation is None:
                self.assertRaises(ValidationError,
                                  field.to_python, datestring)
            else:
                self.assertEqual(field.to_python(datestring),
                                 expectation)

        def test_widget(self):
            from django_iso8601 import ISO8601DateInput
            from django.forms import ValidationError

            widget = ISO8601DateInput(format=format, yeardigits=yeardigits)

            if expectation is not None:
                self.assertEqual(widget._format_value(expectation),
                                 datestring)
            else:
                self.assertEqual(widget._format_value(expectation), None)

    return unittest.TestLoader().loadTestsFromTestCase(TestDate)


def create_datetime_testcase(datetimestring, expectation, format):

    class TestDatetime(BaseTestCase):

        def test_field(self):
            from django_iso8601 import ISO8601DatetimeField
            from django.forms import ValidationError

            field = ISO8601DatetimeField()

            if expectation is None:
                self.assertRaises(ValidationError,
                                  field.to_python, datetimestring)
            else:
                self.assertEqual(field.to_python(datetimestring),
                                 expectation)

        def test_widget(self):
            from django_iso8601 import ISO8601DatetimeInput
            from django.forms import ValidationError

            widget = ISO8601DatetimeInput(format=format)

            if expectation is not None:
                self.assertEqual(widget._format_value(expectation),
                                 datetimestring)
            else:
                self.assertEqual(widget._format_value(expectation), None)

    return unittest.TestLoader().loadTestsFromTestCase(TestDatetime)


def create_time_testcase(timestring, expectation, format):

    class TestTime(BaseTestCase):

        def test_field(self):
            from django_iso8601 import ISO8601TimeField
            from django.forms import ValidationError

            field = ISO8601TimeField()

            if expectation is None:
                self.assertRaises(ValidationError,
                                  field.to_python, timestring)
            else:
                self.assertEqual(field.to_python(timestring),
                                 expectation)

        def test_widget(self):
            from django_iso8601 import ISO8601TimeInput
            from django.forms import ValidationError

            widget = ISO8601TimeInput(format=format)

            if expectation is not None:
                if format is not None:
                    self.assertEqual(widget._format_value(expectation),
                                     timestring)
            else:
                self.assertEqual(widget._format_value(expectation), None)

    return unittest.TestLoader().loadTestsFromTestCase(TestTime)


def test_suite():
    '''
    Construct a TestSuite instance for all test cases.
    '''
    suite = unittest.TestSuite()
    for s, expectation, format in DATE_Y4_TEST_CASES:
        suite.addTest(create_date_testcase(4, s, expectation, format))
    for s, expectation, format in DATE_Y6_TEST_CASES:
        suite.addTest(create_date_testcase(6, s, expectation, format))
    for s, expectation, format in DATETIME_TEST_CASES:
        suite.addTest(create_datetime_testcase(s, expectation, format))
    for s, expectation, format in TIME_TEST_CASES:
        suite.addTest(create_time_testcase(s, expectation, format))
    return suite

def main():
    unittest.main(defaultTest='test_suite')

if __name__ == '__main__':
    main()
