soma = 0
while True:
    try:
        numero = int(input())
        if numero == 0:
            break
        soma = soma + numero
    except EOFError:
        break
print(soma)