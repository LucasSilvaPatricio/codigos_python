
class Boletim:

    def __init__(self):
        self._boletim = []
        self._media = None 

    @property
    def media(self):
        return self._media 
    
    @media.setter
    def media(self,media):
        self._media = media
    
    def inserir_notas(self, materia, notas):
        self._boletim.append({'nome':materia,'notas': notas})

    def listar_boletim(self):
        
        for curso in self._boletim:
            print(f'{40*"="}')
            print(f'boletim do curso de [{curso["nome"]}]')
            for key, nota in enumerate(curso['notas'],start=1):
                print(f'n{key}={nota}')
            print(f'{40*"="}')
# teste da classe
"""
b1 = Boletim()
b1.inserir_notas('matematica',(1,2,3,4))
b1.listar_boletim()

"""



