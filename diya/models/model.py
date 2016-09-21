from mogwai.models import Vertex, Edge


class Data(Vertex):
    no_of_vertex = 0

    def __init__(self, *args, **kwargs):
        if len(*args) > 0:
            self.element_type = args[0]
        else:
            self.element_type = "data"



        super(Data, self).__init__(self, **kwargs)
        Data.no_of_vertex += 1


class Relation(Edge):
    def __init__(self, outV, inV, **kwargs):
        for key, value in kwargs.items():
            if key == 'element_type':
                self.element_type = value
            else:
                self.element_type = "data"
        super(Relation, self).__init__(outV, inV, **kwargs)


class DataFactory:
    def __init__(self):
        pass

    @classmethod
    def create(cls, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'key':
                results = Data.find_by_value(key, value, False)
                if len(results) == 0:
                    return Data.create(*args, **kwargs)
                elif len(results) >= 1:
                    for v in results:
                        data1 = v
                        data1.delete()
                    return Data.create(*args, **kwargs)

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
