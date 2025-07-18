import random
import time
from time import sleep

#Lista Composta e Análise de Dados
dados = []
nome  = []
peso = []
maior_peso = 0
menor_peso = 0
contador_pessoa = 0
while True:
    nome.append(input('Nome: '))
    peso.append(float(input('Peso: ')))
    dados = zip(nome, peso)

    while True:
        respo = input('Deseja Continuar: [S/N] ').upper()[0]
        if respo in ['S', 'N']:
            break
        else:
            print('Resposta Inválida!')
    if respo == 'N':
        break

print(f'Foram Cadastrados {len(nome)} pessoas.')

for c, x in enumerate(peso):
    contador_pessoa += 1
    if contador_pessoa == 1:
        maior_peso = x
        menor_peso = x
    else:
        if x > maior_peso:
            maior_peso = x
        elif x < menor_peso:
            menor_peso = x
if contador_pessoa > 1:
    print(f'O Maior peso foi {maior_peso}Kg. Peso de ', end='')
    for i, n in zip(nome, peso):
        if n == maior_peso:
            print(f'{i} ', end='')
    print()
    print(f'O menor peso foi {menor_peso}Kg. Peso de ', end='')
    for i, n in zip(nome, peso):
        if n == menor_peso:
            print(f'{i} ' , end='')
    print()
elif contador_pessoa == 1:
    print(f'Somente Uma Pessoa Cadastrada. Peso de {maior_peso}Kg.')
else:
    print('Não tem Pessoas Cadastradas!')
from itertools import count

#Lista com pares e ímpares

lista_num = [[], []]

for c in range(7):
    valor = int(input(f'Digite o {c + 1}° Valor: '))

    if valor % 2 == 0:
        lista_num[0].append(valor)
    else:
        lista_num[1].append(valor)
print(f'Os Valores digitados foram {sorted(lista_num)}')
print(f'Os Valores pares digitados foram: {sorted(lista_num[0])}' if len(lista_num[0]) > 0 else 'Não Existe Número Par na Lista!')
print(f'Os valores ímpares digitados foram: {sorted(lista_num[1])}' if len(lista_num[1]) > 0 else 'Não Existe Número Ímpar na Lista!')

#Matrizes
linhas = 3
colunas = 3
lista_matriz = []
valor_par = 0
terceira_coluna = 0
segunda_linha = 0

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o Valor para [{i}][{j}]: '))
        linha.append(valor)

        if valor % 2 == 0:
            valor_par += valor

    lista_matriz.append(linha)
for i in range(linhas):
    terceira_coluna += lista_matriz[i][2]

segunda_linha = max(lista_matriz[1])

print('Matriz Digitada: ')
for linha in lista_matriz:
    print(linha)

print(f'Soma dos Valores Pares: {valor_par}')
print(f'Soma dos Valores da Terceira Coluna: {terceira_coluna}')
print(f'Maior valor da Segunda Linha: {segunda_linha}')

#Palpites para MegaSena
palpite = int(input('Quantos Jogos você quer que eu sorteie? '))
print(f'\n{'=' * 5}Sorteando {palpite} Jogos{'=' * 5}')

for c in range(1, palpite + 1):
    sorteio = sorted(random.sample(range(1, 61), 6))
    print((f'Jogo {c}: {sorteio}'))
    sleep(0.5)
    
print(f'\n{'=' * 5} BOA SORTE {'=' * 5}')

#Boletim de notas com Média

dados = list()
while True:
    nome_aluno = input('Nome: ')
    nota_um = float(input('Nota 01: '))
    nota_dois = float(input('Nota 02: '))
    media_aluno = (nota_um + nota_dois) / 2

    dados.append([nome_aluno, [nota_um, nota_dois], media_aluno] )

    while True:
        cont_respo = input('Deseja Continuar: [S, N] ').upper()[0]
        if cont_respo in ['S', 'N']:
            break
        else:
            print('❌ Respota Inválida. Digite S ou N.')

    if cont_respo == 'N':
        break

print('=' * 50)
print(f'{'N°': <4}{'Nome': <10}{'Média': >8}')
print('-' * 50)
for i, c in enumerate(dados):
    print(f'{i: <4}{c[0]: <10}{c[2]: >8}')

while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual alunos? [999 para parar]: '))
    if opc == 999:
        print('Finalizado!')
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]}: {dados[opc][1]}')
    else:
        print('⚠️ Aluno não encontrado.')
print('Programa Encerrado!')
