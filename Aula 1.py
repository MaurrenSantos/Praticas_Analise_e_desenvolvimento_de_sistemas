nota_1 = int(input("Digite a primeira nota: "))
nota_2 = int(input("Digite a segunda nota: "))
nota_3 = int(input("Digite a terceira nota: "))
nota_4 = int(input("Digite a quarta nota: "))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 6:
    situacao = "Aprovado"

else:
    situacao = "Reprovado"

print (f"A média do aluno é: {media}")
print (f"O aluno está {situacao}")