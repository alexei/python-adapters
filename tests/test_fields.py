# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal
import unittest

import adapters


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
