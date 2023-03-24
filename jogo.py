#tabela do jogo 
#"-" representa vazio
tabuleiro = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

jogadas = 0
symbol_1 = 'X'
symbol_2 = 'O'

#funçao para checkar espaços vazios
def vazio():
    for element in tabuleiro:
        for espaco in element:
            if espaco == "-":
                return False
            else:
                return True

#checkar combinaçoes de vitoria
def win(): 
    #check rows
    for row in range(0,3):
        if tabuleiro[0][row] == tabuleiro[1][row] == tabuleiro[2][row] == symbol_1:
            winner = True
            print("Player " + symbol_1 + ", Voce Ganhou!")
        elif tabuleiro[0][row] == tabuleiro[1][row] == tabuleiro[row][2] == symbol_2:
            winner = True
            print("Player " + symbol_2 + ", Voce Ganhou!")  

    #check cols
    for col in range(0,3):
        if tabuleiro[col][0] == tabuleiro[col][1] == tabuleiro[col][2] == symbol_1:
            winner = True
            print("Player " + symbol_1 + ", Voce Ganhou!")

        elif tabuleiro[col][0] == tabuleiro[col][1] == tabuleiro[col][2] == symbol_2:
            winner = True
            print("Player " + symbol_2 + ", Voce Ganhou!")    

    #check diagonals
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == symbol_1:
        winner = True
        print("Player " + symbol_1 + ", Voce Ganhou!")
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == symbol_1:
        winner = True
        print("Player " + symbol_1 + ", Voce Ganhou!")
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == symbol_2:
        winner = True
        print("Player " + symbol_2 + ", Voce Ganhou!")
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == symbol_1:
        winner = True
        print("Player " + symbol_2 + ", Voce Ganhou!")

    #empate
    if jogadas == 8 and winner (not True):
        print(f"Empate entre o Player {symbol_1} and Player {symbol_2}")

#Mostrar o tabuleiro
def mostrar_tabuleiro():
    print("="*15) 
    for element in tabuleiro:
        print(element)
    print("="*15)       

#Começar o jogo
def start_game(jogadas):
    print("-"*32)
    print("|  Bem-Vindo ao Jogo da velha  |")
    print("-"*32)
    print("O Jogador 'X' começa \n")
    while jogadas in range(0,9):
        mostrar_tabuleiro()
        print("Faça seu próximo movimento sabiamente...\n")
        col = int(input("Escolha uma coluna [1] [2] [3] : "))
        col = col - 1
        row = int(input("Escolha uma linha horizontal [1] [2] [3]: "))
        row = row - 1

        #checkando se ta out of range
        if (row > 3 or row <0) or (col<0 or col > 3):
            print("\nFORA DO TABULEIRO!!!\nTente novamente...")
        #checkando se ja ta preenchido
        elif (tabuleiro[col][row] == symbol_1) or (tabuleiro[col][row] == symbol_2):
            print("\nESSE ESPAÇO JÁ ESTÁ PREENCHIDO!!!\nTente novamente...")
        else:
            if jogadas % 2 == 0:
                tabuleiro[col][row] = "X"
                jogadas = jogadas + 1
            elif jogadas % 2 == 1:
                tabuleiro[col][row] = "O"
                jogadas = jogadas + 1

        win()

        if jogadas == 9:
            print("FIM DO JOGO")

        
        

start_game(jogadas)