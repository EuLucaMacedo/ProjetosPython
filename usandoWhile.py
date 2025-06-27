while True:
    sexo = input('Digite o seu sexo [M/F]: ').upper()
    if sexo in ['M', 'F']:
        break
    else:
        print('Digite uma Opção Valida!\n')

print('Fim do Programa')

intervalo = 10

while True:
    respo = input('\nDeseja Fazer nosso Programa: [S/N] ').upper()
    if respo == 'S':

        termo = int(input('\nDigite o Primeiro Valor da Sequencia: '))
        razao = int(input('Digite o Intervalo entre os Numeros: '))

        while intervalo > 0:
            termo += razao
            intervalo -= 1
            print(f'{termo} ...', end='' )

    else:
        break

print('Acacou')

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

respo = ''
maior_num = 0
menor_num = 100000000
quantos_numeros = 0
soma_num = 0
while True:
    respo = input('Deseja Adicionar um Numero: [S/N] ').upper()
    if respo == 'N':
        break

    num = int(input('Digite um Numero: '))
    if num > maior_num:
        maior_num = num
    if num < menor_num:
        menor_num = num

    soma_num += num
    quantos_numeros += 1

print(f'A Média entre os Número é igual {num/quantos_numeros}')
print(f'O Menor Número digitado foi {menor_num}')
print(f'O Maior Número digitado foi {maior_num}')






