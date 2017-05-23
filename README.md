# Adapters

Adapters allow converting data from one structure to another.

The adapters work very similar to `Serializers` in Django REST framework. They are not tied with Django nor DRF in any way, instead they probide a generic way of transforming an object to another.

The are intended to be used when working with 3rd party APIs and as View-Models.

## Example

Suppose you're dealing with an API that returns a profile in the following format:

    {
        "first_name": "Alexandra",
        "last_name": "Johnson",
        "dob": "2/27/1985",
        "address_street": ["71 Boat Lane"],
        "address_zip": "EH45 0ZQ",
        "address_city": "Alderton",
        "address_country": "GB"
    }

But your local models are a little different:

    class Address(object):
        def __init__(self, **kwargs):
            self.line1 = kwargs.get('line1', None)
            self.line2 = kwargs.get('line2', None)
            self.postal_code = kwargs.get('postal_code', None)
            self.city = kwargs.get('city', None)
            self.region = kwargs.get('region', None)
            self.country = kwargs.get('country', None)


    class Profile(object):
        def __init__(self, **kwargs):
            self.first_name = kwargs.get('first_name', None)
            self.last_name = kwargs.get('last_name', None)
            self.birthday = kwargs.get('birthday', None)
            self.address = kwargs.get('address', None)

How do you create local instances from the result returned by the API? Enter adapters:

    import adapters


    class AddressAdapter(adapters.Adapter):
        class Meta(object):
            model = Address

        line1 = adapters.CharField(source='address_street.0')
        line2 = adapters.CharField(source='address_street.1', default='')
        postal_code = adapters.CharField(source='address_zip')
        city = adapters.CharField(source='address_city')
        region = adapters.CharField(source='address_region', default='')
        country = adapters.CharField(source='address_country')


    class ProfileAdapter(adapters.Adapter):
        class Meta(object):
            model = Profile

        first_name = adapters.CharField()
        first_name = adapters.CharField()
        birthday = adapters.DateField(source='dob')
        address = AddressAdapter(source='*')


    ProfileAdapter().adapt(remote_data)


## Declaring adapters

Declaring an adapter is as simple as inheriting from `adapters.Adapter`.

The `data` argument can be omitted and passed to the `.adapt()` method. See [Adapting data](#adapting-data) below.

The `instance` argument is optional and it allows converting to an existing instance i.e. instead of creating a new one.

### Meta options

The `Meta.model` field specifies the type of the end result. Defaults to `dict` and as such the data is converted to a dictionary.

### Adapting data

To convert data from one format to another, call the `Adapter.adapt()` method. It accepts an optional `data` argument which refers to the data to be converted.

## Fields

Each field accepts the following arguments:

* `source` refers to the attribute that will be used to populate the field; the default is to use the same name as the field;

The `source` argument can use dotted notation to traverse objects e.g. `profile.birthday`.

The value `*` can be used to indicate the adapter to pass the entire object to the field.

* `default` specifies the default value of the resulting field; if not set and the field is required, it will raise an error
* `required` indicates whether the field should be required or not; default is `True`

The following field types are available:

### AdapterMethodField

The field gets it's value by calling a method defined on the adapter class. It can be used to manipulate the data.

The `method_name` argument refers to the name of the method. It defaults to `get_<field_name>`.

### BooleanField

Converts the result to a boolean value.

### CharField

A Unicode field.

### DateField

Parses the value into a `datetime.date` object.

### DateTimeField

Parses the value into a `datetime.datetime` object.

### DecimalField

Parses the value into a `Decimal` object.

### FloatField

A float field.

### IntField

An integer field.

### TimeField

Parses the value into a `datetime.time` object.

### VerbatimField

Copy the value as is.
