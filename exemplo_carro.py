
#import json 

#json_data = [
#    {'nome':'lucas','idade': 22, 'peso':54}
#]

#name_file = 'programa06/database.json'

#with open(name_file, 'w', encoding='utf-8') as arq:
#    json.dump(json_data,arq,ensure_ascii=False,ident=4)

# antes da / é permitido apenas argumentos possicionais.
# depois do * e permitido apenas argumentos possicionais nomeados.
#def soma(a,b,/,*,c,d):
#    print(a,b,c,d)

#soma(1,2,d=3,c=4)
#if __name__ == '__main__':
#    ...


class Carro:
    name_class = 'Carro'

    @classmethod
    def cria_carro_com_esteira(cls,nome):
        return cls(nome,['esteira ' + str(e) for e in range(1,5)])
    
    def __init__(self,nome,pneus=None):
        self.nome = nome
        self.pneus = pneus

    def __getitem__(self,key):
        return self.pneus[key]
    
fusca = Carro('fusca',['pneu 1','pneu 2','pneu 3','pneu 4'])
print(fusca.pneus)

carro_sem_pneu = Carro.cria_carro_com_esteira('fiat')
print(carro_sem_pneu.nome)
print(carro_sem_pneu.pneus)
#print(Carro([3]).name_class)