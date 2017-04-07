# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import adapter
from tests import outputs


class NaturalPersonAdapter(adapter.Adapter):
    first_name = adapter.Field()
    last_name = adapter.Field()


class AddressAdapter(adapter.Adapter):
    class Meta(object):
        model = outputs.Address

    line1 = adapter.Field(source='address_street.0')
    line2 = adapter.Field(source='address_street.1', default='')
    postal_code = adapter.Field(source='address_zipcode', default='')
    city = adapter.Field(source='address_city')
    region = adapter.Field(source='address_state')
    country = adapter.Field(source='address_country')


class CustomerAdapter(NaturalPersonAdapter):
    class Meta(object):
        model = outputs.Customer

    address = AddressAdapter(source='*')


class PersonDictAdapter(adapter.Adapter):
    class Meta(object):
        model = dict

    first_name = adapter.Field(source='first')
    last_name = adapter.Field(source='last')
