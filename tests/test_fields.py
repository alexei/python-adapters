# -*- coding: utf-8 -*-

import datetime
from decimal import Decimal
import unittest

import dateutil.tz

import adapters
import fixtures


class FieldsTest(unittest.TestCase):
    def test_char_field(self):
        actual = adapters.CharField().adapt('Los Angeles')
        expected = 'Los Angeles'
        self.assertEqual(actual, expected)

    def test_int_field(self):
        actual = adapters.IntField().adapt(123456)
        expected = 123456
        self.assertEqual(actual, expected)

    def test_int_field_from_string(self):
        actual = adapters.IntField().adapt('123456')
        expected = 123456
        self.assertEqual(actual, expected)

    def test_float_field(self):
        actual = adapters.FloatField().adapt(3.14159265359)
        expected = 3.14159265359
        self.assertEqual(actual, expected)

    def test_float_field_from_string(self):
        actual = adapters.FloatField().adapt('3.14159265359')
        expected = 3.14159265359
        self.assertEqual(actual, expected)

    def test_decimal_field(self):
        actual = adapters.DecimalField().adapt(0.4032505476)
        expected = Decimal(0.4032505476)
        self.assertAlmostEqual(actual, expected)

    def test_decimal_field_from_string(self):
        actual = adapters.DecimalField().adapt('0.7350977618')
        expected = Decimal(0.7350977618)
        self.assertAlmostEqual(actual, expected)

    def test_boolean_field(self):
        actual = adapters.BooleanField().adapt(True)
        self.assertTrue(actual)

    def test_boolean_field_from_string(self):
        actual = adapters.BooleanField().adapt('Lorem ipsum')
        self.assertTrue(actual)

        actual = adapters.BooleanField().adapt('')
        self.assertFalse(actual)

    def test_boolean_field_from_null(self):
        actual = adapters.BooleanField().adapt(None)
        self.assertFalse(actual)

    def test_time_field(self):
        now = datetime.datetime.today().time()
        actual = adapters.TimeField().adapt(now)
        expected = now
        self.assertEqual(actual, expected)

    def test_time_field_from_string(self):
        tzoffset = dateutil.tz.tzoffset(None, 7200)
        time = datetime.time(13, 14, 15, 16, tzinfo=tzoffset)

        actual = adapters.TimeField().adapt('13:14:15.000016+02:00')
        expected = time
        self.assertEqual(actual, expected)

        actual = adapters.TimeField().adapt('13:14:15.000016')
        expected = datetime.time(13, 14, 15, 16)
        self.assertEqual(actual, expected)

        actual = adapters.TimeField().adapt(time.strftime('%H:%M:%S'))
        expected = datetime.time(13, 14, 15)
        self.assertEqual(actual, expected)

        actual = adapters.TimeField().adapt(time.strftime('%H:%M'))
        expected = datetime.time(13, 14)
        self.assertEqual(actual, expected)

    def test_date_field(self):
        today = datetime.datetime.today().date()
        actual = adapters.DateField().adapt(today)
        expected = today
        self.assertEqual(actual, expected)

    def test_date_field_from_string(self):
        date = datetime.date(1986, 7, 25)
        actual = adapters.DateField().adapt(date.strftime('%Y-%m-%d'))
        expected = date
        self.assertEqual(actual, expected)

    def test_datetime_field(self):
        now = datetime.datetime.today()
        actual = adapters.DateTimeField().adapt(now)
        expected = now
        self.assertEqual(actual, expected)

    def test_datetime_field_from_string(self):
        tzoffset = dateutil.tz.tzoffset(None, 7200)
        time = datetime.datetime(1986, 7, 25, 13, 14, 15, 16, tzinfo=tzoffset)

        data = '1986-07-25 13:14:15.000016+02:00'
        actual = adapters.DateTimeField().adapt(data)
        expected = time
        self.assertEqual(actual, expected)

        data = '1986-07-25 13:14:15.000016'
        actual = adapters.DateTimeField().adapt(data)
        expected = datetime.datetime(1986, 7, 25, 13, 14, 15, 16)
        self.assertEqual(actual, expected)

        data = '1986-07-25 13:14:15'
        actual = adapters.DateTimeField().adapt(data)
        expected = datetime.datetime(1986, 7, 25, 13, 14, 15)
        self.assertEqual(actual, expected)

        data = '1986-07-25 13:14'
        actual = adapters.DateTimeField().adapt(data)
        expected = datetime.datetime(1986, 7, 25, 13, 14)
        self.assertEqual(actual, expected)

    def test_adapter_method_field(self):
        data = [1, 2, 3, 4, 5]
        actual = fixtures.MethodicalAdapter().adapt(data)
        expected = {
            'min': 1,
            'max': 5,
            'sum': 15,
            'avg': 3,
        }
        self.assertDictEqual(actual, expected)
