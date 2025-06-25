import random

ale = random.randint(1, 5)
numero = int(input("Digite um Numero de 1 a 5 e tente a sorte: "))
if numero == ale:
    print(f'\033[34mO Valor Digitado foi {numero}, e o valor Sorteado foi {ale}!\033[m')
    print('\033[34mParabens, você Acertou!!!!\033[m')
else:
    print(f'\033[31OmValor Digitado foi {numero}, e o valor Sorteado foi {ale}!\033[m')
    print('\033[31mTente de Novo!!!\033[m')

respo = input('Deseja continuar? ')
if respo == 'sim':
    velocidade = float(input('Qual a Velocidade que o Carro Percorreu? '))
    if velocidade > 80:
        excesso = velocidade - 80
        multa = excesso * 7
        print(f'\033[31mVocê Foi Multado, o Valor a se pagar R${multa:.2f}\033[m'
              f'')
    else:
        print('Velocidade dentro dos Limites!')
else:
    print('Obrigado por Usar nossos Programas!')

valor = int(input('Digite O valor: '))
resultado = valor % 2
if resultado == 0:
    print('\033[33mO Valor Digitado é Par!')
else:
    print('\033[32mO Valor Digitado é Impar!')

