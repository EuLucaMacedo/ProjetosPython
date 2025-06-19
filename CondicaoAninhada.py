from datetime import datetime

'''valor_casa = float(input('\033[31mQual o Valor da Casa: \033[m'))
salario = float(input('\033[32mQual o Salário: \033[m'))
anos = int (input('\033[33mEm quantos anos faz o pagamento total: \033[m'))

emprestimo = valor_casa / (anos * 12)
por = emprestimo * 30/ 100
if emprestimo <= por:
    print(f'Parabens Emprestimo de {emprestimo: .2f} por mês AUTORIZADO!')
else:
    print(f'Salario não Autorizado para o Emprestimo de {emprestimo: .2f} por mês!')

print("=" * 50)

numero = int(input('\033[35mDigite o Numero que Deseja fazer a conversão: \033[m'))
respo = int(input('\033[31mDigite 1 para Binário, 2 para Octal ou 3 para Hexadecimal: \033[m'))
if respo == 1:
    print(f'{numero} convertido para Binário é igual a {bin(numero)}')
elif respo == 2:
    print (f'{numero} convertido para Binário é igual a {oct(numero)}')
else:
    print(f'{numero} convertido para Binário é igual a {hex(numero)}')

print ("=" * 50)

num_um = int(input('\033[33mDigite o Primeiro Número: '))
num_dois = int (input('Digite o Segundo Número: \033[m'))
if num_um > num_dois:
    print(f'O número {num_um} é maior que o número {num_dois}!')
elif num_um < num_dois:
    print(f'O número {num_um} é menor que o {num_dois}!')
else:
    print(f'Os Números são iguais!')

print('=' * 50)

nascimento = int(input('\033[34mDigite o Ano do seu Nascimento: \033[m'))
ano_atual = datetime.now().year
idade = ano_atual - nascimento
if idade < 18:
    anos = 18 - idade
    print(f'Você tem {idade} anos, ainda nao precisa se Alistar!')
    print(f'Faltam {anos} anos para o Alistamento!')
elif idade > 18:
    anos = idade - 18
    print(f'Você tem {idade} ano, perdeu o Prazo do Alistamento!')
    print(f'Passou {anos} anos do Alistamento!')
else:
    print('Voce Esta na idade de Alistamento, Não perca o Prazo!!!!!')

print('=' * 50)

media_um = float(input('\033[35mDigite a Primeira nota: '))
media_dois = float(input('Digite a Segunda Nota: \033[m'))
media = (media_um + media_dois) / 2
print(f'A média do Aluno é igual a {media}.')
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÂO!')
else:
    print('APROVADO!')

print('=' * 50)

ano_nasc = int(input('\033[36mQual o Ano do Nascimento: \033[m'))
data_atual = datetime.now().year
parabens = data_atual - ano_nasc
print(f'A Idade do Atleta é: {parabens}')
if parabens <= 9:
    print('Classificação: Mirim!')
elif parabens <= 14:
    print('Classificação: Infantil!')
elif parabens <= 19:
    print('Classificação: Junior!')
elif parabens <= 25:
    print('Classificação: Sênior!')
else:
    print('Classificação: Master!')

print('=' * 50)'''

valor_produto = float(input('\033[33mQual o Valor do Produto a ser Pago: R$ '))
pagamento = input('Qual a Condição do Pagamente: \n[ 1 ] Dinheiro\n[ 2 ] Credito\nDigite o Numero da Opção: \033[m')

if pagamento == '1':
    cento = valor_produto * 10/100
    print(f'Pagamento com 10% de Desconto, igual a R${valor_produto - cento}. ')
elif pagamento == '2':
    credito = input("\033[34mPagamento:\n[ 1 ] A Vista\n[ 2 ] 2x\n[ 3 ] 3x\nDigite o Numero da Opção: \033[m")
    if credito == '1':
        cento = valor_produto * 5/100
        print(f'Pagamento com 05% de Desconto, igual a R${valor_produto - cento}.')
    elif credito == '2':
        print(f'Pagamento em Duas Vezes de R${valor_produto/2}.')
    elif credito == '3':
        print(f'Pagamento em Três Vezes de R${valor_produto/3}.')
    else:
        print('Opção Indisponivel!')
else:
    print('Opção Indisponivel!')

print('Obrigado Pelos Códigos!')