# 5 - Faça um Programa que converta metros para centímetros.

while True:
    try:
        num = float(input("Informe um tamanho em \033[0;36mMetro\033[m: "))
        print(f"{num}m é equivalente a {num * 1000}cm")
        break
    except:
        print('\033[0;31mO valor informado não é um número.\033[m')
        continue