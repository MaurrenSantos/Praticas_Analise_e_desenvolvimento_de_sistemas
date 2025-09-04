#Lista de filmes para classificar
filmes = ["Shrek", "Moana", "Vingadores", "Os incríveis", "Homem de aço"]
print ("Bem vindo à classificação de filmes.")
print ("Você tem 5 filmes para classificar.")
print ("Digite '0' a qualquer momento para parar. \n")

# loop para iterar cada filme da lista
for filme in filmes:
    while True:
        classificacao = input(f"Como você classificaria {filme} de 0 à 5? (Digite '0' para parar): ")

        if classificacao == '0':
            print("Você não irá classificar o restante dos filmes")
            # interrompe tanto o while quanto o for
            break

        classificacao = int(classificacao)

        if classificacao < 1 or classificacao > 5:
            print("Por favor, digite um número válido de 1 à 5.")
        else:
            print(f"Você classificou {filme} com {classificacao} estrelas.\n")
            break  # sai do while e vai para o próximo filme

    if classificacao == '0':  # condição para sair do for
        break

print("Obrigado por classificar os filmes!")
