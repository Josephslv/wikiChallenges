# 7 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def handleDoubledArea():
    doubledArea = None

    while doubledArea is None:
        try:
            res = input("Informe a \033[0;33márea\033[m do quadrado (ex: 4m, 20cm, 2km, 300ml): ")

            resNumbers = None

            # Separa o número de tamanho da área da unidade de medida (se tiver).
            if res.isnumeric() is not True:
                resNumbers = []

                resListed = list(res)
                while True:
                    for i in resListed:
                        if i == ',' or i == '.':
                            resNumbers.append('.')

                        if i.isnumeric() is True:
                            resNumbers.append(i)
                    break

                area = float(''.join(resNumbers))
            else:
                area = float(res)
            doubledArea = area * 2

            def response(doubledArea, unit):
                print(f"O dobro da área do quadrado \033[0;33mé de:\033[m {doubledArea}\033[0;33m{unit}\033[m")

            if res.find('km') != -1:
                response(doubledArea, 'km')
                return doubledArea
            if res.find('cm') != -1:
                response(doubledArea, 'cm')
                return doubledArea
            if res.find('ml') != -1:
                response(doubledArea, 'ml')
                return doubledArea
            if res.find('m') != -1:
                response(doubledArea, 'm')
                return doubledArea

            print(f"O dobro da área do quadrado \033[0;33mé de:\033[m {doubledArea}")
            return doubledArea
        except:
            print('\033[0;31mO valor informado não é um número.\033[m')
            continue
        finally:
            restart = input("Deseja calcular novamente? (\033[0;92my\033[mes or \033[0;91mn\033[mo): ")
            if restart == 'y' or restart == 'yes':
                continue
            else:
                if doubledArea is None:
                    return "\033[0;91mErro!\033[m"
                else:
                    return doubledArea
                    

MySquare2 = handleDoubledArea()
print(f"resultado final: \033[0;36m{MySquare2}\033[m")
