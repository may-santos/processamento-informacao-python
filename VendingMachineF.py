def calcular_troco_dp(valor_troco, denominacoes):
    """
    Calcula o menor número de moedas usando programação dinâmica.
    """
    # dp[i] = menor quantidade de moedas para fazer valor i
    dp = [float('inf')] * (valor_troco + 1)
    dp[0] = 0  # 0 moedas para troco 0
    
    for i in range(1, valor_troco + 1):
        for moeda in denominacoes:
            if moeda <= i and dp[i - moeda] != float('inf'):
                dp[i] = min(dp[i], dp[i - moeda] + 1)
    
    return dp[valor_troco] if dp[valor_troco] != float('inf') else -1

def main():
    resultados = []
    while True:
        linha = input().split()
        valor_troco = int(linha[0])
        
        if valor_troco == 0:
            break
        
        num_denominacoes = int(linha[1])
        denominacoes_input = input().split()
        denominacoes = [int(denominacoes_input[i]) for i in range(num_denominacoes)]
        
        resultado = calcular_troco_dp(valor_troco, denominacoes)
        
        if resultado == -1:
            resultados.append("impossivel")
        else:
            resultados.append(str(resultado))
        
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    main()
