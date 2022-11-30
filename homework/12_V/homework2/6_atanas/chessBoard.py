from termcolor import colored

bR = colored("bR", "blue") #The library doesn't work properly help me

board = [[bR,"bK","bB","bQ","KB","bB","bK","bR",],["bP","bP","bP","bP","bP","bP","bP","bP",],
         ["="," ="," ="," ="," ="," ="," ="," =",],["="," ="," ="," ="," ="," ="," ="," =",],
         ["="," ="," ="," ="," ="," ="," ="," =",],["="," ="," ="," ="," ="," ="," ="," =",],
         ["wP","wP","wP","wP","wP","wP","wP","wP",],["wR","wK","wB","wQ","KW","wB","wK","wR",]]

for i in range(8):
    print()
    for j in range (8):
        print(board[i][j], end=" ")
