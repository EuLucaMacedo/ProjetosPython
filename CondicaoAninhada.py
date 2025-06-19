from datetime import datetime

valor_casa = float(input('\033[31mQual o Valor da Casa: \033[m'))
salario = float(input('\033[32mQual o Salário: \033[m'))
anos = int (input('\033[33mEm quantos anos faz o pagamento total: \033[m'))

emprestimo = valor_casa / (anos * 12)
por = (30/ 100) * emprestimo
if salario < por:
    print(f'Salario não Autorizado para o Emprestimo de {emprestimo: .2f} por mês!')
else:
    print(f'Parabens Emprestimo de {emprestimo: .2f} por mês AUTORIZADO!')

print("=" * 50)

numero = int(input('\033[35mDigite o Numero que Deseja fazer a conversão: \033[m'))
respo = int(input('\033[31mDigite 1 para Binário, 2 para Octal ou 3 para Hexadecimal: \033[m'))
if respo == 1:
    print('Binario')
elif respo == 2:
    print ('Octal')
else:
    print('Hexadecimal')

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
if parabens <= 9:
    print('Mirim!')
elif parabens <= 14:
    print('Infantil!')
elif parabens <= 19:
    print('Junior!')
elif parabens == 20:
    print('Sênior!')
else:
    print('Master!')

print('=' * 50)

valor_produto = float(input('\033[33mQual o Valor do Produto a ser Pago: R$'))
pagamento = input('Qual a Condição do Pagamente: \nDinheiro, Cartao, 2x ou 3x\033[m')

if pagamento == 'Dinheiro':
    cento = (10/100) * valor_produto
    print(f'Pagamento com 10% de Desconto, igual a R${cento - valor_produto}. ')
elif pagamento == 'Cartao':
    cento = (5/100) * valor_produto
    print(f'Pagamento com 05% de Desconto, igual a R${cento - valor_produto}.')
elif pagamento == '2x':
    print(f'Pagamento em Duas Vezes de R${valor_produto/2}.')
elif pagamento == '3x':
    print(f'Pagamento em Três Vezes de R${valor_produto/3}.')
else:
    print('Pagamento Indisponivel!')

print('Obrigado Pelos Códigos!')