import calendar
import math
km = float(input('\033[31mDigite Quantos KM serão rodados: \033[m'))
if km > 200:
    valor = 0.45 * km
    print('Percorrendo Mais de 200Km')
    print(f'O Valor da Viagem é de R${valor: .2f}')
else:
    valor = 0.50 * km
    print(f'O Valor da Viagem é de R${valor: .2f}')

ano = int(input('\033[32mEm que ano estamos: \033[m'))
if calendar.isleap(ano):
    print('Ano Bissexto! ')
else:
    print('Não é um ano Bissexto! ')

num1 = float(input('\033[33mDigite o Primeiro Numero: '))
num2 = float(input('Digite o Segundo Numero: '))
num3 = float(input('Digite o Teceiro Numero: \033[m'))

if (num1 > num2 and num1 > num3):
    print(f'O Numero {num1} é Maior que o Numero {num2} e {num3}')

if(num2 > num1 and num2 > num3):
    print(f'O Numero {num2} é Maior que o Numero {num1} e {num3}')

else:
    print(f'O Numero {num3} é Maior que o Numero {num1} e {num2}')

sal = float(input('\033[34mQual o Valor do Salario: \033[m'))
if sal > 1250:
    por = sal * 0.10
    print(f'O salario {sal} teve um aumento para {sal + por}')
else:
    por = sal * 0.15
    print(f'O Salario {sal} teve um aumento para {sal + por}')




