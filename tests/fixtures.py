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
    first_name = adapters.VerbatimField()
    last_name = adapters.VerbatimField()


class LocalAddressAdapter(adapters.Adapter):
    class Meta(object):
        model = LocalAddress

    line1 = adapters.VerbatimField(source='address_street.0')
    line2 = adapters.VerbatimField(source='address_street.1', default='')
    postal_code = adapters.VerbatimField(source='address_zipcode', default='')
    city = adapters.VerbatimField(source='address_city')
    region = adapters.VerbatimField(source='address_state')
    country = adapters.VerbatimField(source='address_country')


class LocalCustomerAdapter(LocalNaturalPersonAdapter):
    class Meta(object):
        model = LocalCustomer

    address = LocalAddressAdapter(source='*')


class PersonDictAdapter(adapters.Adapter):
    first_name = adapters.VerbatimField(source='first')
    last_name = adapters.VerbatimField(source='last')
    birthday = adapters.VerbatimField(source='dob', required=False)


class ListToDictAdapter(adapters.Adapter):
    first_name = adapters.VerbatimField(source='0')
    last_name = adapters.VerbatimField(source='2')
