# O comando import importa uma biblioteca. Aqui foi importado a biblioteca random que gera números aleatórios.
import random
# Foi criada uma váriável palavras para armazenar as palavras que serão sorteadas no jogo(uma lista).
palavras = []
# A variável letrasErradas inicialmente vazia foi criada para armazenar as letras que não corresponderem a palavra sorteada no jogo.
letrasErradas = ''
# Já a variável letrasCertas armazenará as letras que corresponderem a palavra.
letrasCertas = ''
# A variável FORCAIMG contém o desenho das fases do jogo de acordo com o número de acertos ou erros do jogador, será printada na tela a cada palpite.
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# O comando def define uma função que terá uma sequência de comandos, nesse caso def principal é a primeira função do programa.
def principal():
    """
    Função Princial do programa
    """
# O print tem como função imprimir na tela que será rodado o programa.
    print('F O R C A')
     palavrasSugeridas()
# PalavraSecreta é a variável que contém a função sortearPalavra().
    palavraSecreta = sortearPalavra()
# Palpite é a variável  que terá os palpites do jogador sobre as letras que compõem a palavra sorteada.
    palpite = '' 
    desenhaJogo(palavraSecreta,palpite)
# While True é o comando que será executado enquanto a condição for verdadeira.
    while True:
# Nessa parte do programa palpite recebe a função receberPalpite(). 
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
# O comando if é uma instrução que será executada sempre quando a condição for verdadeira,nesse caso chama a funçao perdeuJogo().
        if perdeuJogo():
            print('Voce Perdeu!!!')
# A instrução break quando alcançada quebrará imediatamente o loop while True, saindo de tal.
            break
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
# A função perdeuJogo() é a função que será chamada quando o jogador terminar de colocar seus palpites.        
def perdeuJogo():
# Global é uma instrução que chamará uma variável no programa, ou seja, uma variável que não foi definida "dentro" da função.
    global FORCAIMG
# O comando len vai mostrar a quantidade de intens na lista, nesse programa ele contará a quantidade de letras erradas pelo jogador.
    if len(letrasErradas) == len(FORCAIMG):
# Return True irá retornar dando uma resposta onde for chamado se a função perdeuJogo for verdadeira.
        return True
# else é uma intrução executada sempre que o if não corresponder a condição desejada.    
    else:
# Return False irá retornar onde for chamado indicando que é falso.
        return False
# A função ganhouJogo contém a palavra que foi sorteda, ela recorrerá as letras certas dos palpites do jogador.    
def ganhouJogo(palavraSecreta):
    global letrasCertas
# A variável ganhou recebe verdadeira.
    ganhou = True
# A isntrução 'for' irá percorrer todos os elementos da palavraSecreta verificando se contém a letra palpitada.
    for letra in palavraSecreta:
# Se a letra não pertencer a letrasCertas ganhou receberá falso.
        if letra not in letrasCertas:
            ganhou = False
# Será retornado a variável ganhou indicando se é verdadeiro ou falso.
    return ganhou        
        

# A função receberPalpite é onde o jogador irá palpitar as letras que julga ter na palavra sorteada.
def receberPalpite():
# A variável palpite recebe input(Adivinhe uma letra:) que captura o que é digitado pelo jogador.
    palpite = input("Adivinhe uma letra: ")
# Palpite recebe palpite.upper para deixar as letras palpitadas em maiúsculo. 
    palpite = palpite.upper()
# se a letra for diferente de uma só o programa printará na tela pedindo para digitar uma única letra.
    if len(palpite) != 1:
        print('Coloque uma unica letra.')
# Se não, o programa verificará nas variáveis letrasCertas ou letrasErradas se essa letra já foi dita e printará caso o jogador ja tenha palpitado ela.
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
# Se o que for palpitado não estiver entre "A" e "Z" será pedido que digite apenas letras.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
    else:
        return palpite
    
# A função desenhaJogo contém a apalavra secreta e o palpite, ela recorrerá a global letrasCertas, letrasErradas e FORCAIMG para entẫo printar na tela o desenho da forca como ela atualmente se encontra no jogo.
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
# A variável vazio recebe a quantidade de letras contidas na palavra que foi sorteada e coloca a quantidade de traços para que o jogador tenha uma noção da palavra.
    vazio = len(palavraSecreta)*'-'
# Se o palpite pertencer a palavra sorteada a variável letrasCertas armazenará o palpite somando às letras corretas.
    if palpite in palavraSecreta:
        letrasCertas += palpite
# Se não, isso acontecerá em letrasErradas.
    else:
        letrasErradas += palpite
# letra percorrerá letras certas, range criará uma lista vazia com a quantidade de letras da palavra sorteada, cada espaço vazio será preenchido com a respectiva letra acertada.
    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
# A cada acerto e erro, estes serão printados, assim como a variável vazio que estará printada desde o início do jogo.                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     
# A função sortearPalavra quando chamada recorrerá a global palavras que contém as palavras que poderão ser sorteadas. Sorteará apenas uma palavra e ela retornará.
def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() #choice sorteia uma palavra aleatória na lista.
# A função palavrasSugeridas irá pedir ao jogador que sugira as palavras que deseja que faça parte do jogo, poderão ser adicionadas quantas palavras o jogador desejar, quando ele não digitar será finalizada a lista da variável palavras. 
def palavrasSugeridas():
    global palavras
    while True:
        sugestao= input('Escreva as palavras que deseja para o jogo:')
        palavras.append(sugestao)# append adiciona um item a lista.
        if sugestao== "":
            break


    
principal()
