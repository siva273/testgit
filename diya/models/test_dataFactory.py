from unittest import TestCase

from mogwai.connection import setup

from model import DataFactory

setup('192.168.1.107')


class TestDataFactory(TestCase):
    def setUp(self):
        self.dataFactory = DataFactory()

    def tearDown(self):
        self.dataFactory.despose()
        self.dataFactory = None

    def test_create(self):
        data = 'user'
        details = {'name': 'test', 'age': '20'}

        self.dataFactory.create(data, details)

        self.fail()

    def test_delete(self):
        self.fail()
