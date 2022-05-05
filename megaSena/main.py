import random
from time import sleep

# QUANTOS NUMEROS A PESSOA DESEJA JOGAR


while True:
    QUANTIDADE_DE_NUMEROS = int(input('Quantas DEZENAS deseja apostar [minimo: 6 , maximo: 15]?  '))
    if 5 < QUANTIDADE_DE_NUMEROS < 16:
        QUANTIDADE_DE_NUMEROS = str(QUANTIDADE_DE_NUMEROS)
        break
    else:
        print('Erro Digite entre 6 e 15:')


# CALCULO DO VALOR DE CADA APOSTA

lista_valores = {'6': 4.5, '7': 31.5, '8': 126, '9': 378, '10': 945, '11': 2079, '12': 4158, '13': 7722,
                 '14': 13513.5, '15': 22522.5}
valor_aposta = lista_valores[f'{quantidade_de_numeros}']
print('-' * 40)
print(f'O valor de cada aposta sera de R${valor_aposta}')
sleep(3)
print('-' * 40)
print(f'Agora esta na hora de escolher os seus {quantidade_de_numeros} numeros. ')
print('-' * 40)
sleep(0.5)

# Coletando os numeros do jogador
numeros_escolhidos = []
while len(numeros_escolhidos) != int(quantidade_de_numeros):
    escolha = int(input('Escolha um numero entre 1 e 60: '))
    if escolha in numeros_escolhidos:
        print('Erro voce ja escolheu esse numero.')
    elif 1 > escolha > 60:
        print('Erro! Escolha apenas entre 1 e 60')
    else:
        numeros_escolhidos.append(escolha)
        print(f'Numeros escolhidos -> {numeros_escolhidos}')
        print(f'Voce já escolheu {len(numeros_escolhidos)} de {quantidade_de_numeros}.')
        print('-' * 40)

# Sorteando os numeros e conferindo resultados.
print(f' Seus numeros escolhidos foram {sorted(numeros_escolhidos)}')
numeros_escolhidos = sorted(numeros_escolhidos)
sleep(3)
contador = 0
sena = 0
quina = 0
quadra = 0
while True:
    x = random.sample(range(1, 61), 6)
    x = sorted(x)
    contador += 1
    print(f'{contador}º - {x}')
    lista = []

    for c in x:
        if c in numeros_escolhidos:
            lista.append(c)
    if len(lista) == 6:
        print(f"Voce venceu na Sena com {contador} tentativas.")
        break
    elif len(lista) == 5:
        quina += 1

    elif len(lista) == 4:
        quadra += 1


    elif contador == 10000:
        print(f'Voce nao ganhou nenhuma vez, em {contador} tentativas.')
        break
    lista.clear()
print(f'        ACABOU!      ')
print('-' * 50)
print(f'Voce ganhou {quina} vezes na QUINA.')
print('-' * 50)
print(f'Voce ganhou {quadra} vezes na QUADRA.')
print('-' * 50)
print(f'O custo total das apostas foi de R${contador * valor_aposta}')

