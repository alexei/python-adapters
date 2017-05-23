# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

import fixtures


class AdapterTest(unittest.TestCase):
    def test_object_to_object(self):
        data = fixtures.RemoteCustomer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address_street': ['3385 Gerald L. Bates Drive'],
            'address_zipcode': '02143',
            'address_city': 'Somerville',
            'address_state': 'US-MA',
            'address_country': 'US',
        })
        actual = fixtures.LocalCustomerAdapter(data).adapt()
        expected = fixtures.LocalCustomer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address': fixtures.LocalAddress(**{
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
        data = fixtures.RemoteCustomer(**{
            'first_name': 'Betty',
            'last_name': 'Gowin',
            'address_street': ['3385 Gerald L. Bates Drive'],
            'address_zipcode': '02143',
            'address_city': 'Somerville',
            'address_state': 'US-MA',
            'address_country': 'US',
        })
        instance = fixtures.LocalCustomer()
        actual = fixtures.LocalCustomerAdapter(data, instance=instance).adapt()
        self.assertEqual(actual, instance)

    def test_dict_to_dict(self):
        data = {
            'first': 'Jacquelyn',
            'last': 'Phillips',
        }
        actual = fixtures.PersonDictAdapter().adapt(data)
        expected = {
            'first_name': 'Jacquelyn',
            'last_name': 'Phillips',
        }
        self.assertDictEqual(actual, expected)

    def test_list_to_dict(self):
        data = ['Paul', 'G.', 'Hickey']
        actual = fixtures.ListToDictAdapter().adapt(data)
        expected = {
            'first_name': 'Paul',
            'last_name': 'Hickey',
        }
        self.assertDictEqual(actual, expected)
