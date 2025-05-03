tabuleiro = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

symbol_1 = 'X'
symbol_2 = 'O'
winner = False

def check_tabuleiro_preenchido():
    for element in tabuleiro:
        for espaco in element:
            if espaco == "-":
                return False
    return True
        
def check_vitoria(symbol):
    # Combinações vencedoras: 3 linhas, 3 colunas, 2 diagonais
    combinacoes = [
        # Linhas
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Colunas
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # Diagonais
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]
    for combinacao in combinacoes:
        if all(tabuleiro[x][y] == symbol for x, y in combinacao):
            print(f"Player {symbol}, você ganhou!")
            return True
    return False

def mostrar_tabuleiro():
    print("="*15) 
    for element in tabuleiro:
        print(element)
    print("="*15)    

def apresentacao_jogo():
    print("-"*32)
    print("|  Bem-Vindo ao Jogo da velha  |")
    print("-"*32)
    print("O Jogador 'X' começa \n")

def ler_input_jogador():
    col = int(input("Escolha uma coluna [1] [2] [3] : "))
    col = col - 1
    row = int(input("Escolha uma linha horizontal [1] [2] [3]: "))
    row = row - 1
    return (row, col)

def check_jogada_out_range(row, col):
    if row not in range(3) or col not in range(3):
        return True
    return False

def check_espaco_ocupado(row, col):
    if(tabuleiro[row][col] == '-'):
        return False
    return True

def comecar_jogo():

    jogadas = 0
    apresentacao_jogo()

    while True:
        mostrar_tabuleiro()

        row,col = ler_input_jogador()
        
        if(check_jogada_out_range(row, col)):
            print("\nFORA DO TABULEIRO!!!\nTente novamente...")
        elif (check_espaco_ocupado(row, col)):
            print("\nESSE ESPAÇO JÁ ESTÁ PREENCHIDO!!!\nTente novamente...")
        else:
            symbol = "X" if jogadas % 2 == 0 else "O"
            tabuleiro[row][col] = symbol
            jogadas += 1

        if check_vitoria("X") or check_vitoria("O"):
            mostrar_tabuleiro()
            print("FIM DO JOGO")
            break

        if check_tabuleiro_preenchido():
            mostrar_tabuleiro()
            print("EMPATE!")
            break
        
        

comecar_jogo()