alunos_quantidade = int(input())
banoffe_8_pedacos = int(input())
banoffe_6_pedacos = int(input())

total_fatias = (banoffe_8_pedacos * 8) + (banoffe_6_pedacos * 6)
pedacos_restantes = max(0, total_fatias - alunos_quantidade)

print(pedacos_restantes)