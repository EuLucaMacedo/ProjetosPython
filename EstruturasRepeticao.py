from time import sleep
import datetime

print('Atenção Pela Contagem Regressiva!')

for c in range(10, 0, -1):
    print (c)
    sleep(1)
print('Fim da Contagem')

print('Número Pares Abaixo: ')
for c in range(0, 51, +2):
    print(c)
print("a lista chegou ao fim!")

print('Vamos Calcular os Números!')
mul = 0
print('Calculando ...')
sleep(3)
for c in range(1,500):
    if (c % 3 == 0 and c % 2 != 0):
        mul += c
        
print(f'A soma dos numeros Multiplos de 3 ente 1 e 500 é: {mul}')

numero = int(input('Digite o Numero para a Tabuada: '))
for c in range(1, 11):
    print(f'{c} X {numero} = {c * numero}')
print('Tabuada Concluida!')

print('Numeros Pares!')
soma = 0
for c in range(0, 6):
    par = int(input(f"Digite o {1 + c}° Numero: "))
    if par % 2 == 0 :
        soma += par
print(f'A soma dos Numeros pares é {soma}')

termo = int(input('Digite um Número: '))
razao = int(input('Digite o Valor do Intervalos entre eles: '))

for c in range(10):
    print(f'{termo + c * razao} ... ')
print('Fim da Sequencia!')
ano_atual = datetime.datetime.now().year
quan_menos = 0
quan_mais = 0

for c in range(0, 7):
    nasc = int(input('Digite o ano de Nascimento: '))
    if ano_atual - nasc < 21:
        quan_menos += 1
    else:
        quan_mais += 1

print(f'{quan_menos} Pessoas ainda não tem Maior Idade!')
print(f'{quan_mais} Pessoas já tem Maior Idade!')

peso_maior = 0
peso_menor = 100
for c in range(0, 5):
    peso = float(input('Digite o Peso: '))
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso

print(f'Peso maior é igual a {peso_maior}')
print(f'Peso menor é igaul a {peso_menor}')

idade_Compa = 0
idade_Femi = 0
media = 0
homem_velho = ''

for c in range(0, 4):
    nome = input('Digite o Seu Nome: ')
    idade = int(input('Qual a Sua Idade: '))
    sexo = input('Qual o seu Sexo: [M/F]').upper()

    if idade > idade_Compa and sexo == 'M':
        idade_Compa = idade
        homem_velho = nome

    elif sexo == 'F' and idade < 21:
        idade_Femi += 1

    media += idade

print(f'A Média entre as idades é igual a {media/4}!')
print(f'O Nome do homem mais velho é {homem_velho}!')
print(f'A Quantidade de Mulheres com menos de 21 é Igual a {idade_Femi} mulheres!')






