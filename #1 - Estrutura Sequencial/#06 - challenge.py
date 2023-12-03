# 6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

area = None
while area == None:
    try:
        pi = 3.14159265358979323846
        raio = float(input("Informe o \033[0;33mraio\033[m do círculo: "))
        area = (pi * (raio * raio))
        print(f"Referente ao \033[0;33mraio\033[m, o valor da \033[0;36márea\033[m do cículo é de: \033[0;33m{area:.{2}f}\033[m")
        break
    except:
        print('\033[0;31mO valor informado não é um número.\033[m')
        continue