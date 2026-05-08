
# public
# _protected
# __private
# assosiação, agregação e composição

class Celular:
    
    class_name = 'Celular'

    def __init__(self, marca=None, modelo=None, ram=None, armazenamento=None, cor=None, ):
        self._marca = marca 

    @property
    def marca(self):
        return self._marca

    @marca.setter 
    def marca(self, marca):
        self._marca = marca 
        
    @classmethod
    def get_class_name(cls):
        return cls.class_name
    
c1 = Celular()
print(Celular.get_class_name())
c1.marca = 'Iphone'
print(c1.marca)