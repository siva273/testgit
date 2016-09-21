from mogwai.connection import setup, execute_query
from mogwai.exceptions import MogwaiException
from mogwai.models import Vertex, Edge
from mogwai import properties, relationships
import datetime
from pytz import utc
from functools import partial
from mogwai._compat import print_

setup('192.168.1.131')

class Person(Vertex):
    name = properties.String(required=True, max_length=512, primary_key=True)

class Knows(Edge):
    since = properties.DateTime(required=True, default=partial(datetime.datetime.now, tz=utc))

class Data(Vertex):
    element_type = "data"

    @classmethod
    def createData(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'name':
                results = Data.find_by_value(key, value, False)
                if len(results) == 0:
                    return self.create(*args, **kwargs)
                elif len(results) >= 1:
                    for v in results:
                        data1 = v
                        data1.delete()
                    return self.create(*args, **kwargs)

    def update(self, **values):
        if self.__abstract__:
            raise MogwaiException('cant update abstract elements')
        for key in values.keys():
            if key not in self._manual_values:
                raise TypeError("unrecognized attribute name: '{}'".format(key))

        for k, v in values.items():
            setattr(self, k, v)

        return self.save()

#dharni = Person.create(name='dharni',age=20)
#vijay = Person.create(name='vijay')
#bhargav = Person.create(name='bhargav')
#kiran = Person.create(name='kiran')

data = Data.createData(name="dharni",age="20")
print_(data)
print_(data.keys())
print_(data.values())

updated_data = data.update(name="dharni",age="32")

print_(updated_data)
print_(updated_data.keys())
print_(updated_data.values())

'''
results = Person.find_by_value("name","dharni",False)

print_(type(results))
print_(len(results))

for v in results:
    person = Person()
    person = v
    print_(person)
    person.delete()
    person = Person.create(name="dharni",age=32)
    assert person['age'] == 32
    person.save()
    print_(person.keys())
    print_(person.values())
'''

#if len(Person.find_by_value("name","dharni",False))==0:
    #dharni = Person.create(name="dharni")