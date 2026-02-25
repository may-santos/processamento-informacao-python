while True:
    try:
        linha = input()
        if not linha.strip():
          continue
        valores = linha.split()
        soma = 0
        for item in valores:
            numero = int(item)
            
            if numero == 0:
                break
            soma = soma + numero
        print(soma)
    except EOFError:
        break