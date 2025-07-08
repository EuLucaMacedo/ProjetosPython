import random
#Buscando Numeros na Tupla
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
    n = int(input('Digite um número de 0 a 5: '))
    if 0 <= n <= 5:
        print(f'Você digitou o número: {numeros[n]}')
        break
    else:
        print('Número inválido. Tente novamente.')

#FAzendo analises com Tuplas
times = ('Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Internacional', 'Chapecoense', 'Bahia', 'Cruzeiro')
print(f'Os 5 Primeiros Da Lista: {times[:5]}')
print(f'Os Ultimos Quatro da Lista: {times[-4:]}')
print(f'Lista em Ordem Alfabética: {sorted(times)}')
print(f'O Chapecoence está na {times.index('Chapecoense') + 1}° Posição')

#Sorteio com Tuplas
sorteio = (random.sample(range(1,10), 5))
print(f'os valores sorteados foram: {sorteio}')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')

#Listas com Tuplas
listagem = ('arroz', 1,'papel', 2, 'Biscoito', 7, 'Panela', 10)
print('Listagem de Produtos')
print('='*35)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:<10}................ R${listagem[c + 1]:>7.2f}')
print('='*35)

#Analizando Strings com Tuplas
palavras = ('gato', 'lingua', 'cachorro', 'peixe', 'Hamster')

for palavras in palavras:
    print(f'\nNa Palavra {palavras.upper()} tem as vogais ', end='')
    for vogais in palavras:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
print('Fim do Programa')

#Inserindo Valores na Tupla

núm = ( int(input('Digite um Número: ')),
        int(input('Digite outro Número: ')),
        int(input('Digite mais um Número: ')),
        int(input('Digite o último Número: ')))

print(f'Os valores Digitados foram: {núm}')
print(f'Quantas vezes foram digitados o N° 9: {núm.count(9)}' if 9 in núm else 'Não Contem o Número 9')
print(f'O N° 3 foi digitado na posição {núm.index(3) + 1}' if 3 in núm else 'Não contem o Número 3')
print('Valores Pares Digitados: ', end='')
for c in núm:
    if c % 2 == 0:
        print(f'{c}... ', end='')

print('Fim do Programa!')

