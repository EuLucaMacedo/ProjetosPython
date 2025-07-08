lista = list()
for c in range (1, 6):
    lista.append(int(input(f'Digite o {c}° Número: ')))
maiornumero = sorted(lista)[-1]
segundomaior = sorted(lista)[-2]
print(lista)
print((sorted(lista)))
print(f'Maior Número: {maiornumero}')
print(f'Segundo mmaior Número: {segundomaior}')





