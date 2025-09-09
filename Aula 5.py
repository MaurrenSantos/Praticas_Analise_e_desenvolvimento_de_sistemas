#Solicita ao usuário que insira o valor do produto e o percentual de desconto
valor_produto = float (input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

#Verifica se o percentual de desconto está dentro dos limites aceitáveis
if percentual_desconto < 0 or percentual_desconto > 100:
    print ("Erro! O persentual deve estar dentro dos limites de 0% e 100%")
else:
    desconto = valor_produto * (percentual_desconto / 100)

valor_final = valor_produto - desconto
print (f"O valor final do produto é: R${valor_final:.2f}")