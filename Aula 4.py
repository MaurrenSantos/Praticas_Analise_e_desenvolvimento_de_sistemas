#Cria uma lista
numeros = [1, 2, 3, 4, 5]

comprimento = len(numeros)

print("O comprimento da lista é: ", comprimento)

#Definindo função soma
def soma(a, b):
    resultado = a + b
    return resultado

resultado_soma = soma(5, 3)
print("O resultado da soma é: ", resultado_soma)

#Definindo função "e_par"
def e_par (numero):
    #Operador módulo %
    if numero % 2 == 0:
        return True
    else:
        return False
    
numero = 2148461
if e_par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar")

#Lambda é utilizado como definição uma vez só
soma = lambda a,b: a + b
resultado = soma(3, 4)
print (resultado)

#Refazendo exercício de média:
notas = [7.5, 6.0, 9.3, 10.0, 2.9]

#def para calcular a média
def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

#Função lambda para fazer o arredondamento da média
arredondar_media = lambda media: round(media, 2)

#Calcular média
media = calcular_media(notas)
media_arredondada = arredondar_media(media)

#Situação do estudante
situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

#Resultados
print(f"Essas são suas notas: ", notas)
print(f"Essa é a sua média: ", media_arredondada)
print(f"Você foi: ", situacao)