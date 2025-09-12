#add(), in e remove()

#Criando um conjunto vazio
meu_conjunto = set()

#Adicionando elementos ao conjunto
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)

#Imprimindo o conjunto
print("Conjunto após adicionar elementos: ", meu_conjunto)

#Verificando se um elemento está no conjunto
elemento = 20
if elemento in meu_conjunto:
    print(f"{elemento} está no conjunto")

    #Removendo elemento do conjunto
meu_conjunto.remove(20)
#Imprimindo conjunto atualizado
print("Conjunto após remover o elemento 20: ", meu_conjunto)

############################################################
# Exemplo 1 - Crição de um dicionário vazio, seguido de atribuição de chaves e valores
dici_1 = {}
dici_1['nome'] = "Maria"
dici_1['idade'] = 25

############################################################
# Exemplo 2 - criação de um dicionário com pares chave:  valor
dici_2 = {'nome': 'Maria', 'idade': 25}

# Exemplo 3 - Criação de um dicionário com uma lista de tuplas representando pares chave: valor
dici_3 =  dict([('nome', 'Maria'), ('idade', 25)])

# Exemplo 4 - Criação de um dicionário usando a função built-in zip() e duas listas, uma para as chaves e outra para os valores
dici_4 = dict(zip(['nome', 'idade'], ["Maria", 25]))

# Teste se todas as contruções resultam em objetos iguais
print(dici_1 == dici_2 == dici_3 == dici_4) #Deve imprimir True
print(dici_1)

############################################################
#Importe a biblioteca NumPy
import numpy as np
#Crie um array NumPy de números inteiros
my_array = np.array([1,2,3,4,5])
#Imprima o array
print("Array original: ")
print(my_array)

#Realize operações matemáticas com o array
squared_array = my_array ** 2 #Eleva cada elemento ao quadrado
sum_of_elements = np.sum(my_array) #Calcula a soma de todos os elementos

#Imprima os resultados
print("\nArray ao quadrado: ")
print(squared_array)
print("\nSoma dos elementos: ")
print(sum_of_elements)

#Acesse elementos do array
element_at_index_2 = my_array[2] #Acessa o elemento no índice 2
print("\nElemento no índice 2: ", element_at_index_2)

############################################################
# Importe as bibliotecas necessárias
import numpy as np

# Dados dos participantes
participantes = [
    {
        "nome": "Alice",
        "localização": "EUA",
        "afiliação": "Universidade A",
        "interesses": ["Física", "Astronomia"]
    },
    {
        "nome": "Bob",
        "localização": "Brasil",
        "afiliação": "Instituto B",
        "interesses": ["Biologia", "Astronomia"]
    },
    {
        "nome": "Charlie",
        "localização": "Índia",
        "afiliação": "Instituto C",
        "interesses": ["Química", "Engenharia"]
    }
    # Adicione mais participantes conforme necessário
]

# Usando sets para identificar diferentes regiões dos participantes
regioes = set(participante["localização"] for participante in participantes)

# Usando um dicionário para categorizar afiliações
afiliacoes = {}
for participante in participantes:
    afiliacao = participante["afiliação"]
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante["nome"])

# Usando NumPy para analisar áreas de interesse
areas_de_interesse = np.array(
    [interesse for participante in participantes for interesse in participante["interesses"]]
)
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
area_mais_popular = interesses_unicos[np.argmax(contagem)]

# Resultados
print("Regiões dos participantes: ", regioes)
print("Afiliações dos participantes: ")
for afiliacao, nomes in afiliacoes.items():
    print(f"{afiliacao}: {', '.join(nomes)}")
print("Área de interesse mais popular: ", area_mais_popular)
