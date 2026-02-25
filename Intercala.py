q1 = int(input())
q2 = int(input())

v1 = []
v2 = []

for i in range(0, q1, 1):
    valor = int(input())
    v1.append(valor)

for i in range(0, q2, 1):
    valor = int(input())
    v2.append(valor)

ordenar = v1 + v2
ordenar.sort()

for i in range(0, len(ordenar), 1):
    print(ordenar[i])