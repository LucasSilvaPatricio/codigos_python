# __call__ 
# a função call transforma a instancia em executavel

class Foo:
    def __init__(self, name):
        self.name = name 

    def __call__(self):
        return self.name 
    
foo = Foo('Lucas')
print(foo())