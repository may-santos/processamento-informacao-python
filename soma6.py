
valores = input().split()
soma = 0
for item in valores:
    numero = int(item) 
    if numero == 0:
      break   
    soma = soma + numero


print(soma)