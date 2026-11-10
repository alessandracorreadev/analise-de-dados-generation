# regras: 
# temos que contar de 1 a 100
# se o número é divisível por 3, vamos escrever FIZZ (condição importante)
# se o número é divisível por 5, vamos escrever BUZZ (condição importante)
# se é sivisível por 3 e por 5, vamos escrever FIZZBUZZ (condição mais importante)
# se não, mostra o número (se não combinou com nenhuma condição acima)

for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FIZBUZZ")
    elif numero % 3 == 0:
        print("FIZZ")
    elif numero % 5 == 0:
        print("BUZZ")
    else:
        print(numero)



