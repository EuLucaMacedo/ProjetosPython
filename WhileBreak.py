# Soma de Numeros ate eu digitar 999
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

# Tabuada do numero que eu Desejar
while True:
    tabuada = int(input('Quer ver a tabuada de qual Valor: '))
    print('\n')
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} X {c} = {tabuada * c}')

    print('=' * 50)
print('Programa Tabuada Encerrada. volte sempre!')

#Programa de Analise de Dados
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

#Analisando Produtos
total_gastos = 0
mais_de_mil = 0
nome_produto_barato = ''
mais_produto = ''
preco_mais_barato = 0
contador = 0
while True:
    nome = input('Digite o Nome do Produto: ')
    preco = float(input('Digite o Valor do Produto: '))
    contador =+ 1
    total_gastos += preco
    if preco > 1000:
        mais_de_mil += 1
    if contador == 1:
        preco_mais_barato = preco
    else:
        if preco < preco_mais_barato:
            nome_produto_barato = nome
            preco_mais_barato = preco


    while True:
        mais_produto = input('Deseja Continuar:[S / N] ').upper()[0]
        if mais_produto in ['S', 'N']:
            break
        else:
            print('⚠️ Opção inválida. Digite apenas "S" ou "N".')

    if mais_produto == 'N':
        break

    print('=' * 50)
print(f'O Total da compra foi R${total_gastos}.')
print(f'temos {mais_de_mil} produtos custando mais de R$1000,00.')
print(f'O Produto mais barato foi {nome_produto_barato} com o valor de {preco_mais_barato}')

#Simulador de distribuidor de Notas

sacar = int(input('Valor do Saque:R$ '))
valor_saque = sacar
ced = 50
total_ced = 0

while True:
    if valor_saque >= ced:
        valor_saque -= ced
        total_ced +=1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} Cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced =1
        total_ced = 0
        if valor_saque == 0:
            break
print(f'Volte Sempre!')

