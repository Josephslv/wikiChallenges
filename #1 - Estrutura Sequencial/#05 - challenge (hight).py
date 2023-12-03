# 5 - Faça um Programa que converta metros para centímetros.
centimetro = None
while centimetro == None:
    try:
        metro = float(input("Informe um tamanho em \033[0;36mMetro\033[m: "))
        centimetro = metro * 1000
        print(f"{metro}m é equivalente a {centimetro}cm")
    except:
        print('\033[0;31mO valor informado não é um número.\033[m')
        continue