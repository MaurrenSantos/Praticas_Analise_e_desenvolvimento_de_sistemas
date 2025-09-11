texto = "Explorando a diversidade na linguagem de programação Python."
print(f"Tamanho do texto: {len(texto)}.")
print(f"Python in texto: {'Python' in texto}")
print(f"Quantidade de 'e' no texto: {texto.count('e')}")
print(f"As primeiras 5 letras são: {texto[:5]}")
#################################################
cores = ['vermelho', 'verde', 'amarelo', 'roxo', 'azul']
for cor in cores:
    print(f"Posição = {cores.index(cor)}, cor = {cor}")
#################################################
linguagens = ["Python", "C#", "C++", "Java", "Java Script"]
print("Antes da listcomp: ", linguagens)
linguagens = [item.lower() for item in linguagens]
print("\nDepois da listcomp: ", linguagens)
#################################################
#função map
#aplica uma função em toda sequência
#map (função, sequência)
precos_em_dolares = [100, 50, 85, 240]
taxa_de_cambio = 5.25
precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))
print(precos_em_reais)
#################################################
#Função filter
#filtra os elementos de uma sequência com base em uma função de teste (retorna valor true ou false)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)
#################################################
#A ordem importa--
#Exemplos de mais tuplas e utilidade
vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo do objeto vogais: {type(vogais)}")
for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")

#################################################
#Tupla de convidados
convidados = ("Vanessa", "João", "Maurren", "Cris", "Gilberto")
#Lista de confirmações
confirmados = ["João", "Maurren"]
#Identificar quem ainda não confirmou
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
#Exibir os convidados que ainda não confirmaram
print("Convidados que ainda não confirmaram: ")
for pessoa in nao_confirmados:
    print(pessoa)
#Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram.")