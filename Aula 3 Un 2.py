#Define uma classe chamada Pessoa
class Pessoa:
    # O método __int__ é um construtor, chamado quando um objeto da classe é criado.
    # Ele inicializa os atributos da classe.
    def __init__(self, nome, idade, genero):
        # Self é uma convenção em Python que se refere à própria instância da classe.
        # Os parâmetros nome, idade e gênero são passados durante a criação do objeto.
        # Eles são usados para inicializar os atributos da instância.
        self.nome = nome # Atribui o valor de nome ao atributo nome da instância.
        self.idade = idade # Atribui o valor de idade ao atributo idade da instância.
        self.genero = genero # Atribui o valor de genero ao atributo genero da instância.
    # O método cumprimentar retorna uma saudação com o nome da pessoa.
    def cumprimentar (self):
        return f"Olá, meu nome é {self.nome}."
    # O método aniversario aumenta a iidade da pessoa em 1.
    def aniversario(self):
        self.idade += 1
# Cria uma instânca da classe "Pessoa" com os valores "João", 30 e "Masculino" para nome, idade e genero, respectivamente.
pessoa1 = Pessoa ("João", 30, "Masculino")
# Chama o método "cumprimentar" na instância pessoal e imprime a saudação.
print(pessoa1.cumprimentar()) #Saída: "Olá, meu nome é João"
#Acessa o atributo idade da instância pessoal e imprime a idade.
print(f"Idade: {pessoa1.idade}") # Saída: "Idade: 30"
# Chama o método "aniversário" na instância pessoa1 para aumentar sua idade em 1.
pessoa1.aniversario()
#Acessa o atributo idade atualizado da instância pessoal e imprime a nova idade.
print(f"Nova idade: {pessoa1.idade}") # Saída: "Nova idade: 31"

#################################################################################

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazer_barulho(self):
        pass
class Cachorro(Animal):
    def fazer_barulho(self):
        return "Latir"
class Gato(Animal):
    def fazer_barulho(self):
        return "Miar"
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(f"{rex.nome} faz: {rex.fazer_barulho()}")
print(f"{whiskers.nome} faz: {whiskers.fazer_barulho()}")

#################################################################################

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -= decremento

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.ano}, Velocidade: {self.velocidade} km/h"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia

    def acelerar(self, incremento):
        # Carros podem acelerar mais
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} Km/h"
    
# Criando objetos
carro1 = Carro ("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Moutain Bike", 2021, "MTB")

# Acelerando e verificando o status
carro1.acelerar(50)
bicicleta1.acelerar(20)

# Exibindo o status dos veículos
print("Status do Carro: ")
print(carro1.status())

print("\nStatus da Bicicleta: ")
print(bicicleta1.status())