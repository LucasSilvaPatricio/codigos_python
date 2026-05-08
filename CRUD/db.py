import json 

class Database:
    def __init__(self):
        self._dir_name = ''

    @property 
    def dir_name(self):
        return self._dir_name
    
    @dir_name.setter 
    def dir_name(self,dir_name):
        self._dir_name = dir_name

    def insert(self,query):
        with open(self._dir_name,'w', encoding='utf-8') as arq:
            json.dump(query,arq,indent=2,ensure_ascii=False,)


turma_exemplo =   [
                    { 'name':'c',
                      'turma': {
                            'professor':'p1',
                            'aluno' : 'a1',
                            'disciplinas':'d1,d2,d3'
                      }
                    }
                  ]

db = Database()
db.dir_name = 'database.json'
db.insert(turma_exemplo)