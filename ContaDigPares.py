quantidade_pares = []
while True:
    conta_pares = 0
    try:
        n = input()
        tamanhoN = len(n)
        for i in range(tamanhoN):
            if int(n[i]) % 2 == 0:
                conta_pares += 1
        quantidade_pares.append(conta_pares)    
    except EOFError:
        break

for pares in quantidade_pares:
    print(pares)