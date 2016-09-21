from __future__ import unicode_literals

from mogwai.models import Vertex, Edge


class Data(Vertex):
    def __init__(self, *args, **kwargs):

        if len(args) > 0:
            self.element_type = args[0]
        else:
            self.element_type = 'data'

        super(Vertex, self).__init__(**kwargs)

    @classmethod
    def create(cls, *args, **kwargs):

        return super(Data, cls).create(*args, **kwargs)


class Relation(Edge):
    def __init__(self, outV, inV, **kwargs):
        super(Relation, self).__init__(outV, inV, **kwargs)


class DataFactory:
    def __init__(self):
        pass

    @classmethod
    def create(cls, *args, **kwargs):
        flag_to_create = False
        for key, value in kwargs.items():
            if key == 'key':
                results = Data.find_by_value(key, value, False)
                if len(results) == 0:
                    flag_to_create = True
                elif len(results) >= 1:
                    for v in results:
                        data1 = v
                        data1.delete()
                    flag_to_create = True
        if flag_to_create:
            return Data.create(*args, **kwargs)
        else:
            from diya.models import DiyaModelException
            raise DiyaModelException("Failed to create vertex")

    @classmethod
    def delete(cls, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'key':
                results = Data.find_by_value(key, value, False)
                if len(results) >= 1:
                    for v in results:
                        Data.delete(v)

    @classmethod
    def update(cls, *args, **kwargs):
        pass

    @classmethod
    def search(cls, *args, **kwargs):
        pass


class RelationFactory:
    def __init__(self):
        pass

    @classmethod
    def create(cls, outV, inV, **kwargs):
        pass

    @classmethod
    def delete(cls, *args, **kwargs):
        pass

    @classmethod
    def update(cls, *args, **kwargs):
        pass

    @classmethod
    def search(cls, *args, **kwargs):
        pass
