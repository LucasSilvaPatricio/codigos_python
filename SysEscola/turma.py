from db import DB as db

class Turma:
    @clas
    def __init__(self):
        self._nome_da_turma = None 
        self._professores = []
        self._alunos = []
    
    @property 
    def nome_da_turma(self):
        return self._nome_da_turma
    
    @property
    def professores(self):
        return self._professores
    
    @property
    def alunos(self):
        return self._alunos
    
    @nome_da_turma.setter
    def nome_da_turma(self, nome):
        self._nome_da_turma = nome 
    
    @professores.setter
    def professores(self, professor):
        self._professores.append(professor)

    @alunos.setter
    def alunos(self, aluno):
        self._alunos.append(aluno)
    
    def imprimir(self):
        print('Nome da turma: ',self.nome_da_turma)
        for professor in self._professores:
            print(f'professor: {professor.nome}')
        
        for aluno in self._alunos:
            print(f'Aluno: {aluno.nome}')
            aluno.boletim.listar_boletim()
    
    def cadastrar_turma(self):
        """
        {
            "turma": {
                "name": "turma 7c",
                "alunos": ["aluno1", "aluno2", "aluno3"]
            }
        }
        """
        query_formated = {
            "turma": {
                "turma_nome": self._nome_da_turma,
                "alunos": self._alunos.nome,
            }
        } 

        db.insert(query_formated)
