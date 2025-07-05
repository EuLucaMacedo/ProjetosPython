import random
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco')

while True:
    n = int(input('Digite um número de 0 a 5: '))
    if n == 999:
        break
    if 0 <= n <= 5:
        print(f'Você digitou o número: {numeros[n]}')

    else:
        print('Número inválido. Tente novamente.')

times = ('Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Internacional', 'Chapecoense', 'Bahia', 'Cruzeiro')
print(f'Os 5 Primeiros Da Lista: {times[:5]}')
print(f'Os Ultimos Quatro da Lista: {times[-4:]}')
print(f'Lista em Ordem Alfabética: {sorted(times)}')
print(f'O Chapecoence está na {times.index('Chapecoense') + 1}° Posição')

sorteio = random.sample(range(1,10), 5)
valores = (sorteio)
maior = sorted(valores)[-1]
menor = sorted(valores)[0]
print(f'os valores sorteados foram: {valores}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

listagem = ('arroz', 1,'papel', 2, 'Biscoito', 7, 'Panela', 10)
print('Listagem de Produtos')
print('='*30)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]}................ R${listagem[c + 1]}')

palavras = ('gato', 'lingua', 'cachorro', 'peixe', 'Hamster')

for palavras in palavras:
    print(f'Na Palavra {palavras.upper()} tem as vogais ', end='')
    for vogais in palavras:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')
            print('')