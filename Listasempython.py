maior = 0
menor = 0
contador = 0
posicao_menor = 0
posicao_maior = 0
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
        posicao_maior = c

    elif menor > n:
        menor = n
        posicao_menor = c

print(f'O maior número Digitado foi {maior} na posição {posicao_maior + 1}')
print(f'O menor número digitado foi {menor} na posição {posicao_menor + 1}')
