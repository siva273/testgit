from mogwai.connection import setup
from mogwai._compat import print_

from diya.models import DataFactory, Relation

setup('192.168.1.107')

dharni = DataFactory.create('person',key="dharni",name="dharni",age="20")
vijay = DataFactory.create('person',key="vijay",name="vijay",age="20")

friend = Relation.create(outV=dharni, inV=vijay, name='friends')
employee = Relation.create(outV=dharni, inV=vijay, name='coworker')

edges = Relation.get_between(outV=dharni, inV=vijay)

print_(edges)

for e in edges:
    edge = e
    print_(edge)
    print_(edge.keys())
    print_(edge.values())