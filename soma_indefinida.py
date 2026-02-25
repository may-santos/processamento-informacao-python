try:
    soma = 0
    while True:
        numero = int(input())
        soma += numero
except EOFError:
    print(soma)
