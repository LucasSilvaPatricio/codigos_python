from aluno import Aluno
from boletim import Boletim
from turma import Turma
from professor import Professor


# criação de um aluno
aluno1 = Aluno()
aluno1.nome = 'Maria'
boletim_a1 = Boletim()

boletim_a1.inserir_notas('matematica',(3.4,6.8,9.0,10.0))
boletim_a1.inserir_notas('portugues',(5.4,9.8,5.0,2.0))
boletim_a1.inserir_notas('historia',(5.6,1.5,10.0,9.0))

aluno1._meu_boletim = boletim_a1

aluno2 = Aluno()
aluno2.nome = 'João'
boletim_a2 = Boletim()

boletim_a2.inserir_notas('matematica',(3.4,6.8,9.0,10.0))
boletim_a2.inserir_notas('portugues',(5.4,9.8,5.0,2.0))
boletim_a2.inserir_notas('historia',(5.6,1.5,10.0,9.0))

aluno2._meu_boletim = boletim_a2

#aluno1._meu_boletim.listar_boletim()

# criação dos professores 

professor_1 = Professor()
professor_1.nome = 'Maria'
professor_1.cpf = '234.234.565-23'
professor_1.idade = 45
professor_1.sexo = 'M'

professor_2 = Professor()
professor_2.nome = 'Claudio'
professor_2.cpf = '234.234.565-23'
professor_2.idade = 45
professor_2.sexo = 'M'

professor_3 = Professor()
professor_3.nome = 'Pedro'
professor_3.cpf = '234.234.565-23'
professor_3.idade = 45
professor_3.sexo = 'M'


# criação de uma turma

turma_7c = Turma()
turma_7c.nome_da_turma = '7° ano C'
turma_7c.professores = professor_1
turma_7c.professores = professor_2
turma_7c.professores = professor_3

turma_7c.alunos = aluno1
turma_7c.alunos = aluno2

turma_7c.imprimir()
