# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import adapters


class FieldsTest(unittest.TestCase):
    def test_char_field(self):
        actual = adapters.CharField().adapt('Los Angeles')
        expected = 'Los Angeles'
        self.assertEqual(actual, expected)
