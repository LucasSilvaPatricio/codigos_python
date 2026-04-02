
class Teste:
    def __init__(self):
        self.nome = "Lucas da Silva"
        self.count = 0
        self.new_string = ""
    
    def loop_string(self):
        # loop while
        while(self.count <  len(self.nome)):
            self.new_string += f"* {self.nome[self.count]}"
            self.count += 1
        
        self.new_string += "*"
        print(self.new_string)

Teste().loop_string()
