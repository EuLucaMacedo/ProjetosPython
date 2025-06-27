#Validação de uma Informação
while True:
    sexo = input('Digite o seu sexo [M/F]: ').upper()[0]
    if sexo in ['M', 'F']:
        print(f'Sexo {sexo} Registrado com Sucesso!')
        break
    else:
        print('Digite uma Opção Valida!\n')

print('Fim do Programa')

#Fatorando um Número
fatorial = int(input('Digite um número: '))
i = fatorial
f = 1
print(f'Calculando {fatorial}', end='')
while i > 0:
    print(f'i', end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
    i -= 1


#Sequencia de Fibonacci
n = int(input('Digite a Posição: '))
a = 0
b = 1
posicao = 0

while posicao < n:
    print(f'{a} ... ', end='' )
    c = a + b
    a = b
    b = c
    posicao += 1

print('Acabou!')

#Somando Números
quant_Num = 0
tot_Num = 0
respo = 0
while True:
    respo = int(input('Digite um número: '))
    if respo == 999:
        break
    tot_Num += respo
    quant_Num += 1

print(f'A Quantidade de Numeros Digitados {quant_Num}')
print(f'A Soma entre os Numeros Digitados {tot_Num}')

#Analizando vários valores
respo = ''
maior_num = 0
menor_num = 100000000
quantos_numeros = 0
soma_num = 0
while True:
    try:
        num = int(input('Digite um Numero: '))
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
        continue

    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num

    soma_num += num
    quantos_numeros += 1

    respo = input('Deseja Adicionar um Numero: [S/N] ').upper()[0]
    if respo == 'N':
        break
    elif respo != 'S':
        print('Resposta Invalida!')

if quantos_numeros > 0:
    print(f'A Média entre os Número é igual {soma_num/quantos_numeros}')
    print(f'O Menor Número digitado foi {menor_num}')
    print(f'O Maior Número digitado foi {maior_num}')
else:
    print('\nNenhum número foi digitado.')






