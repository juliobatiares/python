import os
import time

carros = [

     ("Chevrolet Tracker", 120)
    ,("Chevrolet Onix", 90)
    ,("Nissan Kicks", 130)
    ,("Chevrolet Spin", 150)
    ,("Hyundai HB20", 85)
    ,("Ford Ka", 85)
    ,("Fiat Uno", 70)
    ,("Fiat Pulse", 130)
]

alugados = []

#criando uma função para trabalhar com minha tupla
def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i,car[0],car[1]))

#mostrar_lista_de_carros(carros)

while True:
    os.system("clear")
    print("=================================================")
    print("..:: Bem vindo a Loja de Aluguel de Carros! ::..")
    print("=================================================")
    print("")
    print(">>> O que deseja fazer?")
    print("")
    print("0 - Mostrar Portifólio | 1 - Alugar um Carro | 2 - Devolver um Carro")

    op = int(input())

    os.system("clear")
    
    time.sleep(1)

    if op == 0:
        pass

    elif op == 1:
        pass

    elif op == 2:
        pass

    
    print("")
    print("====================")
    print("0 para CONTINUAR | 1 para SAIR")

    if int(input()) == 1:
        break

