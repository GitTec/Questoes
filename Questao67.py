#Um  segurança de um templo recebe cristãos, judeus e muçulmanos, crie um programa que ao final do dia
# ira dizer a quantidade de cristãos de judeus e muçulmanos frequentaram o templo


print("*"*30)
print("     NOSSO TEMPLO RECEBE")
print("CRISTAO -- JUDEU -- MUCULMANO")
print("*"*30)

cristaos=0
judeus=0
muculmanos=0

while True:
    entrada=input("INFORME QUEM ENTROU: ")

    if entrada == "ACABOU":
        print("NÃO TEM MAIS NINGUEM PRA ENTRAR")
        break
    if entrada =="CRISTAO":
        cristaos += 1
        print("ENTROU O CRISTÃO")
    elif entrada == "JUDEU":
        judeus += 1
        print("ENTROU O JUDEU")
    elif entrada == "MUCULMANO":
        muculmanos += 1
        print("ENTROU O MUÇULMANO")
    else:
        print("O TEMPLO NÃO RECEBE ESSE TIPO")

cont=cristaos+judeus+muculmanos
print("*"*40)
print("QUANTIDADES DE FREQUENTADORES DO TEMPLO")
print("*"*40)
print(f"TORAL GERAL FOI --> {cont} SENDO")
print(f"{cristaos} CRISTÃOS ")
print(f"    {judeus} JUDEUS ")
print(f"        {muculmanos} MUÇULMANOS ")
print("*"*40)