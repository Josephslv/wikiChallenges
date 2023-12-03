# 2 - Faça um Programa que peça um número e então mostre a mensagem (O número informado foi [número])

while True:
    try:
        num = int(input("Porfavor, informe um número: "))
        print(f"\033[0;32mO número informado foi\033[m {num}\033[0;32m!\033[m")
        break
    except:
        print('\033[0;31mO valor informado não é um número.\033[m')
        continue