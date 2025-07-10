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