#Uma escola de ensino médio deseja que o professor digite o nome de todos os alunos que irão para
# uma viagem ao museu quando o professor digitar FIM deve exigir a quantidade de alunos que irão para viagem
# e seus nomes

print("*"*25)
print("VIAGEM PARA O MUSEU ")
print("*"*25)

alunos=[]

while True:
    nome=input("INFORME O NOME DO ALUNO: ")
    if nome == "FIM" or nome == "fim":
        print("ACABARAM OS ALUNOS")
        break
    alunos.append(nome)

print("*" * 40)
print(f"OS {len(alunos)} ALUNOS QUE VÃO SAO:")
for el in alunos:   #AQUI ACESSO CADA ELEMENTO DIRETO DO ARRAY
    print(el)
print("*"*40)

#for i in range(len(alunos)):   #CONTO AS POSIÇÕES E CRIO UM FOR DO TAMANHO DO ARRAY
#    print(alunos[i])

