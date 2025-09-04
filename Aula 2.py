#Aplicando a aula
print ("Bem vindo ao cinema!")

idade = int(input("Por favor, digite sua idade: "))

if idade < 12:
    print ("Indicamos filme infantil 1")
elif idade >= 12 and idade < 18:
    print ("Indicamos filme adolescente 2")
else:
    print ("Indicamos filme 3")

quantidade_ingressos = 10
if quantidade_ingressos == 0:
    print ("Ingressos esgotados!")
else:
    print ("Compre seus ingressos aqui!")
