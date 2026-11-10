def main():
    # 1 - Criando as listas iniciais
    produtos = ["Camiseta Básica", "Calça Jeans", "Jaqueta Corta-Vento"]
    precos = [49.90, 129.90, 219.90]

    # Mostrando o estoque
    print("ESTOQUE".center(50, '-'))
    for produto, preco in zip(produtos, precos):
            print(f"{produto} -R${preco:.2f}")
    print('-'*50)

    # 2 - cadastrar um novo produto
    print("CADASTRAR PRODUTO".center(50, '-'))
    novo_produto = input("Nome do produto: ")
    novo_preco = float(input("Preço do produto: "))
    produtos.append(novo_produto)
    precos.append(novo_preco)
    print('-'*50)

    print("ESTOQUE".center(50, '-'))
    for produto, preco in zip(produtos, precos):
        print(f"{produto} -R${preco:.2f}")
    print('-'*50)

    # 3 - Remover o último produto e mostrar o que foi removido
    if len(produtos) > 0 and len(precos) > 0:
        produto_removido = produtos.pop()
        preco_removido = precos.pop()
        print(f"O produto removido foi {produto_removido} \nO preço removido foi {preco_removido:.2f}")

    else:
         print("Estoque vazio")
    
    # for i in range(len(produtos)):
    #  print(f"{produtos[i]}", {precos[i]})

    # 4 - Removendo por nome

    print("REMOVER PRODUTO".center(50, '-'))
    remover_produto = input("Nome do produto a ser removido: ")

    if remover_produto in produtos:
        index_produto = produtos.index(remover_produto)
        produtos.remove(remover_produto)
        precos.pop(index_produto)
        print(f"Produto {remover_produto} e seu preço R${precos[index_produto]:.2f} removido.")
    else:
        print("Produto não encontrado.")

    print('-'*50)

if __name__ == "__main__":
    main()

