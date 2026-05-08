from pessoa import Pessoa 

class Aluno(Pessoa):
    def __init__(self):
        self._turma = None
        self._meu_boletim = None
        self._nome = None 

    @property
    def turma(self):
        return self._turma
    
    @turma.setter 
    def turma(self, turma):
        self._turma = turma

    @property
    def nome(self):
        return self._nome
    
    @nome.setter 
    def nome(self, nome):
        self._nome = nome

    @property
    def boletim(self):
        return self._meu_boletim
    
    @boletim.setter 
    def boletim(self, boletim):
        self._meu_boletim = boletim

