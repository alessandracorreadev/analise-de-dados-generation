produtos = ["Banana", "Melancia", "Jambolão"]
precos = [5, 19, 29.99]

print("Bem Vindo ao Varejão da Generation".center(50, '-'))

print("PRODUTOS".center(50, '-'))

for i, j in zip(produtos, precos):
    print(f"{i} - R${j:.2f}")

escolha = input("Deseja cadastrar um novo produto? [sim/nao]: ")

if escolha.lower() == "sim":
    novo_produto = input("Nome do produto: ")
    novo_preco = float(input("Preço do produto: "))

produtos.append(novo_produto)
precos.append(novo_preco)

for i, j in zip(produtos, precos):
    print(f"{i} - R${j:.2f}")