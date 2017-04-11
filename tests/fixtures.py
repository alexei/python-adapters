# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import adapters


class Struct(object):
    def __init__(self, **data):
        self.__dict__.update(data)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class RemoteCustomer(Struct):
    pass


class LocalCustomer(Struct):
    pass


class LocalAddress(Struct):
    pass


class LocalNaturalPersonAdapter(adapters.Adapter):
    first_name = adapters.Field()
    last_name = adapters.Field()


class LocalAddressAdapter(adapters.Adapter):
    class Meta(object):
        model = LocalAddress

    line1 = adapters.Field(source='address_street.0')
    line2 = adapters.Field(source='address_street.1', default='')
    postal_code = adapters.Field(source='address_zipcode', default='')
    city = adapters.Field(source='address_city')
    region = adapters.Field(source='address_state')
    country = adapters.Field(source='address_country')


class LocalCustomerAdapter(LocalNaturalPersonAdapter):
    class Meta(object):
        model = LocalCustomer

    address = LocalAddressAdapter(source='*')


class PersonDictAdapter(adapters.Adapter):
    first_name = adapters.Field(source='first')
    last_name = adapters.Field(source='last')
    birthday = adapters.Field(source='dob', required=False)


class ListToDictAdapter(adapters.Adapter):
    first_name = adapters.Field(source='0')
    last_name = adapters.Field(source='2')
