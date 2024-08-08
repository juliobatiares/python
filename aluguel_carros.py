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
    
    print("abrindo Portifólio...")
    print("")
    time.sleep(1)

    os.system("clear")

    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print("")
        print("Escolha o código do carro que deseja alugar:")
        cod_carro = int(input())
        print("Por quantos dias você deseja alugar este carro?:")
        dias = int(input())

        os.system("clear")

        print("Você escolheu o carro {} por {} dias.".format(carros[cod_carro][0],dias))
        print("")
        print("Total do aluguel: R${},00. \nDeseja Alugar?".format(carros[cod_carro][1] * dias))
        print("")
        print("0 - SIM | 1 - NÃO")
        conf = int(input())
        if conf == 0:
            print("Parabéns! Você alugou o {} por {} dias.".format(carros[cod_carro][0],dias))
            alugados.append(carros.pop(cod_carro))

    elif op == 2:
        if len(alugados) == 0:
            print("Não há nenhum carro locado.")
        else:
            print("Segue a lista de carros alugados. Qual você deseja devolver?")
            mostrar_lista_de_carros(alugados)
            print("")
            print("Escolha o código do carro que deseja devolver:")
            dev = int(input())

            print("Obrigado por devolver o carro {}.".format(alugados[dev][0]))
            carros.append(alugados.pop(dev))

    print("")
    print("====================")
    print("")
    print("0 para CONTINUAR | 1 para SAIR")

    if int(input()) == 1:
        break

