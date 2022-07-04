#Um médico deve fazer uma lista de todas as doenças que ele diagnosticou no dia, crie um agoritmo pra isso

print("*"*40)
print("RELAÇAO DE DOENÇAS")
print("*"*40)

doencas=[] #AQUI DENTRO VAI FICAR A LISTA DAS DOENÇAS
while True:
    nomDoenca=input("INFORME O NOME DA DOENÇA: ")
    if nomDoenca == "FIM" or nomDoenca == "fim":
        print("-" * 40)
        print("ESSAS FORAM AS DOENÇAS DIAGNOSTICADAS")
        break
    doencas.append(nomDoenca)
print("-"*40)
for i in range(len(doencas)):
    print(f"DOENÇA {i+1}= {doencas[i]}")
