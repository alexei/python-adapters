# -*- coding: utf-8 -*-

from __future__ import unicode_literals

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
