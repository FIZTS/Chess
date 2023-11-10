class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♙ '
        else:
            self.symbol = ' ♟ '


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♖ '
        else:
            self.symbol = ' ♜ '


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♘ '
        else:
            self.symbol = ' ♞ '


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♗ '
        else:
            self.symbol = ' ♝ '


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♕ '
        else:
            self.symbol = ' ♛ '


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♔ '
        else:
            self.symbol = ' ♚ '


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
        print("    a  b  c  d  e  f  g  h")
        for i, row in enumerate(self.board, 1):
            print(f"{i} ", end="")
            for piece in row:
                if piece is None:
                    print(' . ', end='')
                else:
                    print(piece, end='')
            print(f" {i}")

    def is_valid_move(self, start, end, color):
        if any(coord < 0 or coord >= 8 for coord in start + end):
            return False
        if start == end or self.board[start[0]][start[1]] is None:
            return False
        piece = self.board[start[0]][start[1]]
        if piece.color != color:
            return False
        return True

    def move_piece(self, start, end):
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = None

# main game loop
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
        elif chess_board.is_valid_move(start, end, 'black'):
            chess_board.move_piece(start, end)
        else:
            print("Invalid move. Try again.")
