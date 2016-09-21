from mogwai.connection import setup
from mogwai.models import Vertex
from models import model

setup('192.168.1.132')

Person = type('Person', (Vertex,), {})

dharni = Person.