n1 = float(input("digite sua nota em Matemática : "))
n2 = float(input("digite sua nota em Português : "))
n3 = float(input("digite sua nota em História :  "))
n4 = float(input("digite sua nota em Quimíca : "))

notas = [n1, n2, n3, n4]

print(f"Sua maior nota foi {max(notas)}, durante o bimestre parabéns, e sua menor nota foi {min(notas)},  a média das suas notas foi:.")

media = sum(notas)/len(notas)
print (media)

if media >=5:
    print("aprovado")
else:
    print("reprovado")