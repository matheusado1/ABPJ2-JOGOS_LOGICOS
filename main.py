import random

print("Jogo da Adivinhação")

numero_secreto = random.randint(1, 100)

tentativas = 0

while True:
    try:
        palpite = int(input("Digite um número entre 1 e 100: "))
        
        if palpite < 1 or palpite > 100:
            print(" Digite um número válido entre 1 e 100!")
            continue

        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f" Acertou em {tentativas} tentativas!")
            break

    except ValueError:
        print("Digite apenas números inteiros!")
