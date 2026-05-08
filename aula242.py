# __str__, __repr__, {self.y!r}, __add__, __gt__, __new__, __init__, __enter__, __exit__

class OpenFile:
    def __init__(self, name_file, mode):
        self._name_file = name_file
        self._mode = mode 
        self._file = None 

    def __str__(self):
        return f'({self._name_file},{self._mode})'

    def __repr__(self):
        return f'(self._name_file={self._name_file!r},self._mode={self._mode!r})'
    
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._file = open(self._name_file, self._mode, encoding='utf-8')
        return self._file
    
    def __exit__(self, class_exception_, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._file.close()

    def __sum__(self, value):
        return 
     
of = OpenFile('teste.txt','w')
print(repr(of))
with of as f:
    f.write('Ok, funcionou')

"""
class Geometry:

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        print('ok')


    def calc_square(self):
        square = self.x * self.y 
        return square 
    
    def calc_rect(self):
        rectangle = self.x * self.y 
        return rectangle
    
#gm = object.__new__(Geometry)

"""