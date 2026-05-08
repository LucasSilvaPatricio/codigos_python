#-*-coding:utf8;-*-

import os
import time

os.system("clear")

class Pessoa():

    def __init__(self):

        # atributos de pessoa

        self.altura = None
        self.peso = None
        self.cor_do_cabelo = None

        print("Você acaba de criar uma pessoa\n")


    def setAltura(self, altura):
        self.altura = altura

    def setPeso(self, peso):
        self.peso = peso

    def setCordocabelo(self,cor_do_cabelo):
        self.cor_do_cabelo = cor_do_cabelo


    def getAltura(self):
        return self.altura

    def getPeso(self):
        return self.peso

    def getCordocabelo(self):
        return self.cor_do_cabelo

    # methodos de pessoa

    def andar(self):
        return "Andando\n"

    def comer(self):
        return "Comendo\n"

    def falar(self):
        return "Falando\n"

    def dormir(self):
        return "Dormindo\n"

    def dormir(self):
        print("pessoa está dormindo não acorde ela, espere ela acordar zZzZzz...\n")
        time.sleep(10)
        print("Agora ela acordou\n")

    def escrevendo(self):
        print("pessoa está digitando uma mensagem para você.\n")
        texto = "Olá Humano"
        for letra in texto:
            time.sleep(0.2)
            print(letra, end="", flush=True)
        time.sleep(1)
        print("\n")

pessoa = Pessoa()
pessoa .escrevendo()

