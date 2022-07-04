

print("*"*25)
print("VIAGEM PARA O MUSEU ")
print("*"*25)

alunos=[]
qtdAlunos=int(input("QUANTOS ALUNOS VÃO AO MUSEU? "))

for i in range(qtdAlunos):
    nome=input(f"INFORME O {i+1}°ALUNO-> ")

    if nome == "FIM" or nome == "fim":
        print("ACABARAM OS ALUNOS")
    alunos.append(nome)

print("*"*40)
print("AQUI ESTÃO OS ALUNOS QUE VÃO AO MUSEU")
print("-"*40)
print(f"O(S) {qtdAlunos} ALUNO(A) QUE VÃO AO MUSEU SÃO: ")
for aluno in alunos:
    print(aluno)
print("*"*40)
