def jogar():

    enforcou = False
    acertou = False
    Erro = 7
    
    tela_abertura()

    palavra_secreta = load_palavra_secreta()
    
    lista_palavra = lista_palavra_secreta(palavra_secreta)
   
    while(not enforcou and not acertou):
        
        chute = jogada()

        if(chute in palavra_secreta):
            valida_jogada(palavra_secreta,lista_palavra,chute)
        else:
            Erro -= 1  
            desenha_forca(Erro)     

        jogadas = "".join(lista_palavra)
        acertou = jogadas == palavra_secreta
        enforcou = Erro == 0
    
    finaliza_jogo(acertou)
    rerun()

def tela_abertura():
    print("**********************************")
    print("****Bem vindo ao jogo da Forca****")
    print("**********************************")

def load_palavra_secreta():
    palavra_secreta = input("Digite uma palavra pra alguém adivinhar: ").upper()
    return palavra_secreta

def lista_palavra_secreta(palavra):
    lista_palavra = []
    for l in palavra:
        lista_palavra.append("_")
    return lista_palavra

def jogada():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def valida_jogada(palavra,lista,chutes):
    index = 0
    for letra in palavra:
        if(chutes == letra):
            lista[index] = letra
        index = index +1 
    print(lista)

def finaliza_jogo(acertou):

    if(acertou):        
        return print('Parabéns, você venceu')
    else:
        return print('Você perdeu, tente novamente') 

def rerun():
    respota = input("Deseja jogar novamente? [S] Sim [N] Não  ").strip().upper()
    if (respota == "S"):
        jogar()
    else:
        print("Obrigado por jogar")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):    
    jogar()


