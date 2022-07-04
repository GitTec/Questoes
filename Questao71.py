#Um médico atende homens e mulheres, ao final do dia deseja exibir quantidades de homens e de mulheres
# que atendeu, crie um algoritmo que faça isso para ele.
print("*"*30)
print("ATENDIMENTO HOMENS E MULHERES")
print("*"*30)

masc=0
femin=0

while True:
    nome=input("INFORME QUEM ENTROU: ")

    if nome == "FIM" or nome == "fim":
        print("-"*30)
        print("ENCERRAMOS OS ATENDIMENTOS""")
        break
    if nome == "HOMEM" or nome == "homem":
        masc += 1
    elif nome == "MULHER" or nome == "mulher":
        femin += 1
    else:
        print("NÃO SE ENCAIXA EM NOSSOS ATENDIMENTOS")

total=masc+femin
print("*"*40)
print(f"TIVEMOS {total} ATENDIMENTO(S), SENDO:")
if masc == 1:
    print("1 HOMEM")
else:
    print(f"{masc} HOMENS ")
if femin == 2:
    print("1 MULHER")
else:
    print(f"{femin} MULHERES")
print("*"*40)