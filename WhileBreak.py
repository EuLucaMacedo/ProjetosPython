n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um Numero: '))
    if n == 999:
        break
    else:

        s += s + n
        c += 1

print(f'Foram Digitados {c} números e a soma deles é igual a {s}!')

tabuada = 0

while True:
    tabuada = int(input('Quer ver a tabuada de qual Valor: '))
    print('\n')
    if tabuada < 0:
        print('Programa Tabuada Encerrada. volte sempre!')
        break
    for c in range(1, 11):
        print(f'{tabuada} X {c} = {tabuada * c}')

    print('=' * 50)


idade = 0
sexo = ''
continuar = 's'
maior_idade = 0
homens = 0
mulheres = 0
while True:
    print('CADASTRO DE PESSOA')

    while True:
        try:
            idade = int(input('Digite a Idade: '))
            if idade < 0 or idade > 130:
                print('⚠️ Idade inválida. Digite um valor entre 0 e 130.')
            else:
                break
        except ValueError:
            print('❌ Entrada inválida. Digite apenas números inteiros.')

    while True:
        sexo = input('Digite o Sexo:[ M / F ] ').upper()[0]
        if sexo in ['M' , 'F']:
            break
        else:
            print('⚠️ Sexo inválido. Digite apenas "M" ou "F".')
    print('=' * 50 )

    if idade >= 18:
        maior_idade += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    while True:
        continuar = input('Deseja Continuar? [S / N] ').upper()[0]
        if continuar in ['S', 'N']:
            break
        else:
            print('⚠️ Opção inválida. Digite apenas "S" ou "N".')
    print('=' * 50)

    if continuar == 'N':
        break

print(f'Total de Pessoas com mais de 18 anos: {maior_idade}')
print(f'{homens} Homens Cadastrados!')
print(f'{mulheres} Mulheres com menos de 20 anos Cadastradas!')

nome = ''
preco = 0
total_gastos = 0
mais_de_mil = 0
nome_produto_barato = ''
mais_produto = ''
preco_mais_barato = 0
while True:
    nome = input('Digite o Nome do Produto: ')
    preco = float(input('Digite o Valor do Produto: '))

    total_gastos += preco
    if preco > 1000:
        mais_de_mil += 1
    if preco < 1000:
        nome_produto_barato = nome
        preco_mais_barato = preco


    while True:
        mais_produto = input('Deseja Continuar:[S / N] ').upper()[0]
        if mais_produto in ['S', 'N']:
            break
        else:
            print('⚠️ Opção inválida. Digite apenas "S" ou "N".')

    print('=' * 50)
    if mais_produto == 'N':
        break

print(f'O Total da compra foi R${total_gastos}.')
print(f'temos {mais_de_mil} produtos custando mais de R$1000,00.')
print(f'O Produto mais barato foi {nome_produto_barato} com o valor de {preco_mais_barato}')


