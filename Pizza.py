quantidade_estudantes = int(input())
quantidade_pizzas = int(input())
quantidade_pizzas_pequena = int(input())

pedacos_grande = quantidade_pizzas * 8
pedacos_pequena = quantidade_pizzas_pequena * 6

total_pedacos = pedacos_grande + pedacos_pequena

restaram = total_pedacos - quantidade_estudantes

if restaram < 0:
    print("0")
else:
    print(restaram)
