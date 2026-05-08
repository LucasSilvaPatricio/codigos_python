import os 
os.system('cls')
print('===============INICIO=================')
# FCFS
processos = [
    {"ID": "P1", "Chegada": 1, "Rajada": 8, "Prioridade": 2},
    {"ID": "P2", "Chegada": 1, "Rajada": 3, "Prioridade": 1},
    {"ID": "P3", "Chegada": 2, "Rajada": 1, "Prioridade": 3},
    {"ID": "P4", "Chegada": 10, "Rajada": 15, "Prioridade": 5},
    {"ID": "P5", "Chegada": 15, "Rajada": 8, "Prioridade": 1},
    {"ID": "P6", "Chegada": 20, "Rajada": 20, "Prioridade": 2},
    {"ID": "P7", "Chegada": 23, "Rajada": 8, "Prioridade": 4},
    {"ID": "P8", "Chegada": 30, "Rajada": 14, "Prioridade": 3},
    {"ID": "P9", "Chegada": 40, "Rajada": 6, "Prioridade": 2}
]


tempo_total = 40
def generator(processos, tempo):

    def executar(proc):
        for r in range(1,(proc['Rajada']+1)):
            print(f'executando processo{proc["ID"]} rajada {proc["Rajada"]}: {r}')

    tempo = 1
    executado = set()
    
    for i in range(1,41):
        
   
        for proc in processos:
            if proc['Chegada'] == i:
                executado.update([proc['Chegada']])
                print(f'Execução no tempo {tempo}')
                executar(proc)
                if not proc['Chegada'] in executado:
                    tempo = tempo + proc['Rajada']
                

        if not i in executado:   
            print(f'Tempo {i} sem processos')  
        tempo = tempo + 1
        

        print()
        print()
        



#for processo in processos:
generator(processos,tempo_total)
