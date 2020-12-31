print("*****************************************************************************")
print("*********************** BEM-VINDO AO JOGO DA FORCA!!! ***********************")
print("*****************************************************************************\n")

palavra_secreta = "banana"
enforcou = False
acertou = False

while not enforcou and not acertou:

    chute = input("Qual a letra?")
    index = 0

    for letra in palavra_secreta:
        if chute == letra:
            print("Encontrei a letra {} na posição {}".format(letra, index))
        index = index + 1
    print("Jogando")
print("Fim de jogo!")