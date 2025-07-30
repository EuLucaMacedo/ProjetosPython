'''lista = list()
for c in range (1, 6):
    lista.append(int(input(f'Digite o {c}° Número: ')))
maiornumero = sorted(lista)[-1]
segundomaior = sorted(lista)[-2]
print(lista)
print((sorted(lista)))
print(f'Maior Número: {maiornumero}')
print(f'Segundo mmaior Número: {segundomaior}')'''

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()

    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")

    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])

    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

# Exibe os itens e o total da compra
for item, preco in carrinho:
    print(f'{item}: R${preco:.2f}')

print(f'Total: R${total:.2f}')
