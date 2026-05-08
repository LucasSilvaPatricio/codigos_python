from abc import ABC, abstractmethod 

class LogMixin(ABC):
    
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def setlog(self):...

class MyOpen(LogMixin):
    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.my_file = None 

    def setlog(self):
        super().__init__('ErrorClose:')

        with open('logerror.txt','w',encoding='utf8') as arquivo:
            arquivo.write(self.title+'Error no close')      
    
    def __enter__(self):
        print('Arquivo aberto')
        self.my_file = open(self.file_dir, 'w', encoding='utf-8')
    
    def __exit__(self,class_exception_,exception_,traceback_):
        self.setlog()
        self.my_file.close()

with MyOpen('dados2.txt') as arquivo:
    ...

