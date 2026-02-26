media_falta = input().split()
media = float(media_falta[0])
faltas = int(media_falta[1])

if media >= 6.0 and faltas <= 30:
    print("Aprovado!")