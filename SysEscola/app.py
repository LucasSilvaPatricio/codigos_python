from turma import Turma 
from aluno import Aluno 
from functools import partial


cmd = None
while cmd != 'exit':
    print('[insert-turma] para cadastrar turma')
    cmd = input('Digite um comando: ')

    if cmd == 'insert-turma':
        turma = Turma()
        
        turma_nome = input('Nome da turma: ')
        turma.nome_da_turma = turma_nome
        
        quant = input('Quantidade de alunos: ')

        alunos = []
        for i in range(0,int(quant)):
            nome_aluno = input('Nome do aluno: ')
            aluno = Aluno().nome = nome_aluno
            alunos.append(aluno)

        alunos_nome = [aluno for aluno in alunos]
        print(alunos_nome)
        turma.cadastrar_turma()
    
    