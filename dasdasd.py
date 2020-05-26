class heranca:
    pass
pai_caracter = heranca()

mae_caracter = heranca()

pai_caracter.olhos = "Olhos Verdes"
mae_caracter.cabelo = "Cabelos Pretos"


cont = 0
while cont < 4:
    if cont == 0:
        pergunta = input("Digite Pai").upper()
        cont+=1
    elif cont == 1:
        pergunta = input("Digite Mae").upper()
        cont += 1
    elif cont == 2:
        pergunta = input("Digite filho").upper()
        cont += 1
    elif cont == 3:
        pergunta = input("Digite filha").upper()
        cont += 1
    if pergunta == "PAI":
        print("\033[1m {}\033[m".format(pai_caracter.olhos))
    elif pergunta =="MAE":
        print("\033[1m {}\033[m".format(mae_caracter.cabelo))
    elif pergunta == "FILHO":
        print("\033[1m {} herdados do meu Pai\033[m".format(pai_caracter.olhos))
    elif pergunta == "FILHA":
        print("\033[1m {} herdados da minha mãe\033[m".format(mae_caracter.cabelo))
    else:
        cont+= 1