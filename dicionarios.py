dados = dict()

dados['nome'] = str(input('Nome Aluno: '))
dados['media'] = float(input(f'Média de {dados['nome']}: '))
print(f'Nome: {dados['nome']}')
print(f'Média do Aluno: {dados['media']}')

if dados['media'] >= 7:
    print('Situação é igual a Aprovado!')
else:
    print('Situação é igual a Reprovado!')
