# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import unittest

import adapters
import inputs
import outputs


class AdapterTest(unittest.TestCase):
    def test_object_to_object(self):
        data = inputs.Customer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address_street': ['3385 Gerald L. Bates Drive'],
            'address_zipcode': '02143',
            'address_city': 'Somerville',
            'address_state': 'US-MA',
            'address_country': 'US',
        })
        actual = adapters.CustomerAdapter(data).adapt()
        expected = outputs.Customer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address': outputs.Address(**{
                'line1': '3385 Gerald L. Bates Drive',
                'line2': '',
                'postal_code': '02143',
                'city': 'Somerville',
                'region': 'US-MA',
                'country': 'US',
            })
        })

        self.assertEqual(actual.first_name, expected.first_name)
        self.assertEqual(actual.last_name, expected.last_name)
        self.assertEqual(actual.address.line1, expected.address.line1)
        self.assertEqual(actual.address.line2, expected.address.line2)
        self.assertEqual(
            actual.address.postal_code, expected.address.postal_code)
        self.assertEqual(actual.address.city, expected.address.city)
        self.assertEqual(actual.address.region, expected.address.region)
        self.assertEqual(actual.address.country, expected.address.country)

    def test_object_to_existing_object(self):
        data = inputs.Customer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address_street': ['3385 Gerald L. Bates Drive'],
            'address_zipcode': '02143',
            'address_city': 'Somerville',
            'address_state': 'US-MA',
            'address_country': 'US',
        })
        instance = outputs.Customer()
        actual = adapters.CustomerAdapter(data, instance=instance).adapt()
        self.assertEqual(actual, instance)

    def test_dict_to_dict(self):
        data = {
            'first': 'Jacquelyn',
            'last': 'Phillips',
        }
        actual = adapters.PersonDictAdapter().adapt(data)
        expected = {
            'first_name': 'Jacquelyn',
            'last_name': 'Phillips',
        }
        self.assertDictEqual(actual, expected)

    def test_list_to_dict(self):
        data = ['Paul', 'G.', 'Hickey']
        actual = adapters.ListToDictAdapter().adapt(data)
        expected = {
            'first_name': 'Paul',
            'last_name': 'Hickey',
        }
        self.assertDictEqual(actual, expected)
