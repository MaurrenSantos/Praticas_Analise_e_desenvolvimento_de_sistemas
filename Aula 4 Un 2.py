# Primeiro modo
import math

math.sqrt(25)
math.log2(1024)
math.cos(45)

# Segundo modo
import math as m 

m.sqrt(25)
m.log2(1024)
m.cos(45)

# Terceiro modo
from math import sqrt, log2, cos

sqrt(25)
log2(1024)
cos(45)

#####################################################################

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3 ,5]

# Criar um gráfico de linha
plt.plot(x, y)

# Adicionar rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')


# Adicionar um título ao gráfico
plt.title("Exemplo de Gráfico de Linha")

# Mostrar o gráfico
plt.show()

#########################################################

import matplotlib.pyplot as plt

# Dados de exemplo
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas = [120, 90, 150, 80, 200, 300 , 100, 60, 70, 95, 310, 400]

# Criar um gráfico de barras
plt.bar(meses, vendas, color='yellow')

#Adicionar rótulos aos eixos
plt.xlabel('Mês')
plt.ylabel('Vendas(em unidades)')

#Adicionar título ao gráfico
plt.title('Vendas mensais')

#Mostrar o gráfico
plt.show()