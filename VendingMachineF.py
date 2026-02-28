def calcular_troco_guloso(valor_troco, denominacoes):
    denominacoes_ordenadas = sorted(denominacoes, reverse=True)
    quantidade_total = 0
    valor_restante = valor_troco
    
    for denominacao in denominacoes_ordenadas:
        if valor_restante >= denominacao:
            qtd = valor_restante // denominacao
            quantidade_total += qtd
            valor_restante -= qtd * denominacao
    
    if valor_restante > 0:
        return -1
    
    return quantidade_total

def main():
    resultados = []
    while True:
        linha = input().split()
        valor_troco = int(linha[0])
        
        if valor_troco == 0:
            break
        
        num_denominacoes = int(linha[1])
        denominacoes = list(map(int, input().split()))
        
        resultado = calcular_troco_guloso(valor_troco, denominacoes)
        
        if resultado == -1:
            resultados.append("impossivel")
        else:
            resultados.append(str(resultado))

    for res in resultados:
        print(res)

if __name__ == "__main__":
    main()