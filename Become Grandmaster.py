'''
8*8 mattrix
7 types of pieces = 7 move patterns
2 sides (black and white)
import picture (chess.com or download)

make a screen

Turn
    - White turn
    - White Select
        - White select new pieces
            -White select possible move
        - White select possible move
    - Black turn
        - Black select new pieces
            -White select possible move
        - White select possible move

captured pieces are thrown to the side of the board became smaller
remind check with highlighting

game ended with check and no escape
    - How about stalement??

Restart game
    - Should the board be flipped??
'''

#maybe this project is too hard na 
'''
import pygame

class King:
    pass

pos_letter = "abcdefgh"
pos_number = "12345678"
blank = []
white_king = ['wK']
white_queen = ['wQ']
white_rook = ['wR0','wR1']
white_knight = ['wN0','wN1']
white_bishop = ['wB0','wB1']
white_pawn = ['wP0','wP1','wP2','wP3','wP4','wP5','wP6','wP7']




board_called = [['a8','a7','a6','a5','a4','a3','a2','a1']
['b8','b7','b6','b5','b4','b3','b2','b1'],
['c8','c7','c6','c5','c4','c3','c2','c1'],
['d8','d7','d6','d5','d4','d3','d2','d1'],
['e8','e7','e6','e5','e4','e3','e2','e1'],
['f8','f7','f6','f5','f4','f3','f2','f1'],
['g8','g7','g7','g5','g4','g3','g2','g1'],
['h8','h7','h7','h5','h4','h3','h2','h1']]


board_pieces = [['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
[blank,blank,blank,blank,blank,blank,blank,blank],
[blank,blank,blank,blank,blank,blank,blank,blank],
[blank,blank,blank,blank,blank,blank,blank,blank],
[blank,blank,blank,blank,blank,blank,blank,blank],
[white_pawn[0], white_pawn[1], white_pawn[2], white_pawn[3], white_pawn[4], white_pawn[5], white_pawn[6], white_pawn[7]],
[white_rook[0], white_knight[0], white_bishop[0], white_queen, white_king, white_bishop[1], white_knight[1], white_rook[1]]]

print(board_pieces)
'''

class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'white':
            self.symbol = ' ♟ '
        else:
            self.symbol = ' ♙ '


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        #self.symbol = ' ♖ ' if color == 'white' else ' ♜ '
        if color == 'white':
            self.symbol = ' ♜ '


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = ' ♘ ' if color == 'white' else ' ♞ '


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = ' ♗ ' if color == 'white' else ' ♝ '


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = ' ♕ ' if color == 'white' else ' ♛ '


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = ' ♔ ' if color == 'white' else ' ♚ '


class ChessBoard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]

    def initialize_board(self):
        for i in range(8):
            self.board[1][i] = Pawn('white')
            self.board[6][i] = Pawn('black')
        self.board[0][0] = Rook('white')
        self.board[0][7] = Rook('white')
        self.board[7][0] = Rook('black')
        self.board[7][7] = Rook('black')
        self.board[0][1] = Knight('white')
        self.board[0][6] = Knight('white')
        self.board[7][1] = Knight('black')
        self.board[7][6] = Knight('black')
        self.board[0][2] = Bishop('white')
        self.board[0][5] = Bishop('white')
        self.board[7][2] = Bishop('black')
        self.board[7][5] = Bishop('black')
        self.board[0][3] = Queen('white')
        self.board[7][3] = Queen('black')
        self.board[0][4] = King('white')
        self.board[7][4] = King('black')

    def print_board(self):
        print("  a  b  c  d  e  f  g  h")
        for i, row in enumerate(self.board, 1):
            print(f"{9 - i} ", end="")
            for piece in row:
                if piece is None:
                    print(' . ', end='')
                else:
                    print(piece, end='')
            print(f" {9 - i}")

    def is_valid_move(self, start, end, color):
        if start == end or self.board[start[0]][start[1]] is None:
            return False
        piece = self.board[start[0]][start[1]]
        if piece.color != color:
            return False
        return True

    def move_piece(self, start, end):
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = None

#main game na
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.initialize_board()
    while True:
        chess_board.print_board()
        start = input("Enter the starting position (e.g., 'a2'): ")
        end = input("Enter the ending position (e.g., 'a4'): ")

        start = (int(start[1]) - 1, ord(start[0]) - ord('a'))
        end = (int(end[1]) - 1, ord(end[0]) - ord('a'))

        if chess_board.is_valid_move(start, end, 'white'):
            chess_board.move_piece(start, end)
        else:
            print("Invalid move. Try again.")
