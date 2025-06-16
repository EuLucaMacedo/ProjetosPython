import random

ale = random.randint(1, 5)
numero = int(input("Digite um Numero de 1 a 5 e tente a sorte: "))
if numero == ale:
    print(f'O Valor Digitado foi {numero}, e o valor Sorteado foi {ale}!')
    print('Parabens, você Acertou!!!!')
else:
    print(f'O Valor Digitado foi {numero}, e o valor Sorteado foi {ale}!')
    print('Tente de Novo!!!')

respo = input('Deseja continuar? ')
if respo == 'sim':
    velocidade = float(input('Qual a Velocidade que o Carro Percorreu? '))
    if velocidade > 80:
        excesso = velocidade - 80
        multa = excesso * 7
        print(f'Você Foi Multado, o Valor a se pagar R${multa:.2f}')
    else:
        print('Velocidade dentro dos Limites!')
else:
    print('Obrigado por Usar nossos Programas!')

valor = int(input('Digite O valor: '))
if valor % 0 :
    print('O Valor Digitado é Par!')
else:
    print('O Valor Digitado é Impar!')

