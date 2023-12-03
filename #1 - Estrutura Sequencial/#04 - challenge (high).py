# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def redTxt(text):
    return f"\033[0;31m{text}\033[m"
def greenTxt(text):
    return f"\033[0;31m{text}\033[m"

def handleNoteValue(bimestre):
    while True:
        try:
            nota = float(input(f"Informe a nota do {bimestre}º bimestre: "))

            if nota > 10:
                print(f"{redTxt('OBS: A nota deverá ter um valor')} MENOR {redTxt('ou')} IGUAL {redTxt('a')} 10{redTxt('!')}")
                continue
            if nota < 0:
                print(f"{redTxt('OBS: A nota deverá ter um valor')} MAIOR {redTxt('ou')} IGUAL {redTxt('a')} 0{redTxt('!')}")
                continue
            return nota
        except:
            print('\033[0;31mO valor informado não é um número.\033[m')
            continue


nota1 = handleNoteValue(1)
nota2 = handleNoteValue(2)
nota3 = handleNoteValue(3)
nota4 = handleNoteValue(4)

notaTotal = nota1 + nota2 + nota3 + nota4
media = notaTotal / 4
print(f"Sua nota total é de \033[0;32m{notaTotal}\033[m, assim obtendo uma média de: \033[0;32m{media}\033[m")