print("  *********************************************************************")
print("  *********************** ESCOLHA O SEU JOGO!!! ***********************")
print("  *********************************************************************\n")

jogo = input("Digite 1 para o Teste Jedi ou 2 para o Jogo da Forca!!!\n")

if jogo == "1":
    import advinhacao
elif jogo == "2":
    import forca
else:
    print("Só aceitamos 1 ou 2 como resposta para escolher o Jogo!\n")