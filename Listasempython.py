#Maior e menor Número
maior = 0
menor = 0
contador = 0
listanumerica = list()
for c in range(0,5):
    listanumerica.append(int(input(f'Digite o {c + 1}° Numero: ')))
print(f'Lista Digitada: {listanumerica}')

for c, n in enumerate(listanumerica):
    contador += 1
    if contador == 1:
        maior = n
        menor = n

    elif maior < n:
        maior = n

    elif menor > n:
        menor = n

print(f'O maior número Digitado foi {maior} na posição ', end='')
for i, v in enumerate(listanumerica):
    if v == maior:
        print(f'{i + 1}... ', end='')
print()
print(f'O menor número digitado foi {menor} na posição ', end='')
for i, v in enumerate(listanumerica):
    if v == menor:
        print(f'{i + 1}... ', end='')
print()

#Adicionando um número na lista sem se repetir!
num = []
while True:
    valor = (int(input('Digite Um Número: ')))

    if valor not in num:
        num.append(valor)
        print('Número Adicionado com Sucesso ...')

    else:
        print('Valor Duplicado! Não Adicionado na Lista!')



    respo = input('Deseja Continuar: [S/N] ').upper()[0]
    while True:
        if respo in ['S', 'N']:
            break
        else:
            print('Resposta ìnvalida:')

    if respo == 'N':
        break

print(f'Números Adicionados: {sorted(num)}')

#Extraindo dados de uma Lista

numeros_digitados = []

while True:

    while True:
        try:
            numeros_digitados.append(int(input('Digite um Número: ')))
            if numeros_digitados[-1] < 0:
                print('Digite um Valor válido!')
            else:
                break
        except ValueError:
            print('❌ Entrada inválida. Digite apenas números inteiros.')

    while True:
        respo = input('Deseja Continuar: [S/N]').upper()[0]
        if respo in ['S', 'N']:
            break
        else:
            print('Digite um valor Válido!')

    if respo == 'N':
        break

print(f'Numero Digitados: {numeros_digitados}')
print(f'Foram Digitados {len(numeros_digitados)} números!')
print(f'Ordem decrescente dos numero digitados: {sorted(numeros_digitados, reverse = True )}')
print(f'O Número 5 foi encontrado na Lista na Posição {numeros_digitados.index(5)}' if 5 in numeros_digitados else 'Número 5 não está na Lista')

#Lista de Números Pares e Ímpares
numeros_alinhados = []
while True:
    while True:
        try:
            verificando_numero = int(input('Digite um Número: '))
            if verificando_numero < 0 :
                print('❌ Digite um Número Válido!')
            else:
                numeros_alinhados.append(verificando_numero)
                break

        except ValueError:
            print('❌ Entrada inválida. Digite apenas números inteiros.')

    while True:
        continuar_programa = input('Deseja Continuar: [S/N] ').upper()[0]
        if continuar_programa in ['S', 'N']:
            break
        else:
            print('❌ Digite um valor válido!')

    if continuar_programa == 'N':
        break

numeros_par = []
numeros_impar = []
print(f'Lista dos Número digitados {numeros_alinhados}')
for c in numeros_alinhados:
    if c % 2 == 0:
        numeros_par.append(c)
    else:
        numeros_impar.append(c)
print(f'Lista de Números Pares: {numeros_par}' if len(numeros_par) > 0 else 'Não Existe Números Pares na Lista!')
print(f'Lista de Números Ímpares: {numeros_impar}' if len(numeros_impar) > 0 else 'Não Existe Números Ímpares na Lista!')

#Inserindo na Lista

ordem = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > ordem[-1]:
        ordem.append(n)
        print('Adicionado ao final da lista ...')
    else:
        pos = 0
        while pos < len(ordem):
            if n <= ordem[pos]:
                ordem.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista ...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {ordem}')



