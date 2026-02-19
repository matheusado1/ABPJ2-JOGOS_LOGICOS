print("Jogo da Adivinhação")

numero_secreto = 7  
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Acertou em {tentativas} tentativas!")
        break
