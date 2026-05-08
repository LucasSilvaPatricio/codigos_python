from aluno import Aluno 

class App:
    def __init__(self):
        ...
    
    @staticmethod
    def menu():
        print('======== Funções disponiveis ========')
        print('cadastrar aluno: [CAD-A]luno')
        

loop = True

app = App()

while loop:
    app.menu()
    cmd = input('cmd: ')
    
    if 'CAD-A' in cmd.upper():
        Aluno().cadastrar_aluno()

    if cmd.lower() == 'exit':
        break 

