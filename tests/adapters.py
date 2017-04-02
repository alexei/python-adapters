# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import

import adapter
from tests import outputs


class NaturalPersonAdapter(adapter.Adapter):
    first_name = adapter.CharField()
    last_name = adapter.CharField()


class AddressAdapter(adapter.Adapter):
    class Meta(object):
        model = outputs.Address

    line1 = adapter.CharField(source='address_street.0')
    line2 = adapter.CharField(source='address_street.1', default='')
    postal_code = adapter.CharField(source='address_zipcode', default='')
    city = adapter.CharField(source='address_city')
    region = adapter.CharField(source='address_state')
    country = adapter.CharField(source='address_country')


class CustomerAdapter(NaturalPersonAdapter):
    class Meta(object):
        model = outputs.Customer

    address = AddressAdapter(source='*')
