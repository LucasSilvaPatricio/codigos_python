class Aluno:

  def __init__(self,professor=None, disciplina=None):
    
    # dados pessoais
    self._nome = None
    self._cpf = None
    self._email = None 
    self._tel = None 

    self._professor = professor 
    self._disciplina = disciplina 
  
  @property 
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self,nome):
    self._nome = nome
  
  @property 
  def cpf(self):
    return self._cpf
  
  @cpf.setter
  def cpf(self,cpf):
    self._cpf = cpf
  
  @property 
  def email(self):
    return self._email
  
  @email.setter
  def email(self,email):
    self._email = email
  
  @property 
  def tel(self):
    return self._tel
  
  @tel.setter
  def tel(self,tel):
    self._tel = tel

  def cadastrar_aluno(self):
        print('Vamos cadastrar um novo aluno, preciso que digite as informações pessoas dele.')
    
        nome = input('Nome: ')
        cpf = input('CPF: ')
        email = input('E-mail: ')
        telefone = input('Tel: ')

        aluno = Aluno()
        aluno.nome = nome 
        aluno.cpf = cpf 
        aluno.email = email 
        aluno.tel = telefone

        
      