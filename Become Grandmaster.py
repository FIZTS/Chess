class ChessPiece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.symbol

    def valid_moves(self, start, end, board):
        raise NotImplementedError("Subclasses must implement the valid_moves method")


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♙ '
        else:
            self.symbol = ' ♟ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end
        direction = 1 if self.color == 'white' else -1

        if col_start == col_end and board[row_end][col_end] is None:
            if row_end == row_start + direction:
                return True
            elif row_end == row_start + 2 * direction and row_start in [1, 6] and board[row_start + direction][col_start] is None:
                return True

        elif abs(col_start - col_end) == 1 and row_end == row_start + direction:
            target_piece = board[row_end][col_end]
            if target_piece is not None and target_piece.color != self.color:
                return True

        return False


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♖ '
        else:
            self.symbol = ' ♜ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end
        return row_start == row_end or col_start == col_end


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♘ '
        else:
            self.symbol = ' ♞ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end

        # Calculate the absolute differences in row and column
        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)

        # Check if the move is an L-shape: two squares in one direction and one square in a perpendicular direction
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = board[row_end][col_end]
            # Check if the target square is empty or contains an opponent's piece
            if target_piece is None or target_piece.color != self.color:
                return True

        return False


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♗ '
        else:
            self.symbol = ' ♝ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end

        # Check if the move is diagonal
        if abs(row_end - row_start) == abs(col_end - col_start):
            # Check if there are no pieces blocking the diagonal path
            step_row = 1 if row_end > row_start else -1
            step_col = 1 if col_end > col_start else -1

            i, j = row_start + step_row, col_start + step_col
            while i != row_end and j != col_end:
                if board[i][j] is not None:
                    return False  # Blocked by another piece
                i += step_row
                j += step_col

            target_piece = board[row_end][col_end]
            # Check if the target square is empty or contains an opponent's piece
            if target_piece is None or target_piece.color != self.color:
                return True

        return False


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♕ '
        else:
            self.symbol = ' ♛ '

class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♕ '
        else:
            self.symbol = ' ♛ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end

        # Check if the move is horizontal, vertical, or diagonal
        is_horizontal = row_start == row_end
        is_vertical = col_start == col_end
        is_diagonal = abs(row_end - row_start) == abs(col_end - col_start)

        # Check if there are no pieces blocking the path
        if is_horizontal:
            step_col = 1 if col_end > col_start else -1
            j = col_start + step_col
            while j != col_end:
                if board[row_start][j] is not None:
                    return False  # Blocked by another piece
                j += step_col
        elif is_vertical:
            step_row = 1 if row_end > row_start else -1
            i = row_start + step_row
            while i != row_end:
                if board[i][col_start] is not None:
                    return False  # Blocked by another piece
                i += step_row
        elif is_diagonal:
            step_row = 1 if row_end > row_start else -1
            step_col = 1 if col_end > col_start else -1
            i, j = row_start + step_row, col_start + step_col
            while i != row_end and j != col_end:
                if board[i][j] is not None:
                    return False  # Blocked by another piece
                i += step_row
                j += step_col
        else:
            return False  # Invalid move

        target_piece = board[row_end][col_end]
        # Check if the target square is empty or contains an opponent's piece
        if target_piece is None or target_piece.color != self.color:
            return True

        return False

class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        if color == 'black':
            self.symbol = ' ♔ '
        else:
            self.symbol = ' ♚ '

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end

        # Check if the move is one square away in any direction
        is_horizontal = row_start == row_end and abs(col_end - col_start) == 1
        is_vertical = col_start == col_end and abs(row_end - row_start) == 1
        is_diagonal = abs(row_end - row_start) == 1 and abs(col_end - col_start) == 1

        if is_horizontal or is_vertical or is_diagonal:
            target_piece = board[row_end][col_end]
            # Check if the target square is empty or contains an opponent's piece
            if target_piece is None or target_piece.color != self.color:
                return True

        return False


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
        return piece.valid_moves(start, end, self.board)

    def move_piece(self, start, end):
        if self.is_valid_move(start, end, self.board[start[0]][start[1]].color):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = None

        # Check if either king is missing
            white_king_exists = any(isinstance(piece, King) and piece.color == 'white' for row in self.board for piece in row)
            black_king_exists = any(isinstance(piece, King) and piece.color == 'black' for row in self.board for piece in row)

            # Print game end message if either king is missing
            if not white_king_exists or not black_king_exists:
                print("!!!!!!!!!!!!!!!!!!!!Game Over!!!!!!!!!!!!!!!!!!!!")
                exit()
    

if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.initialize_board()
    while True:
        chess_board.print_board()
        start = input("Enter the starting position (e.g., 'a2'): ")
        end = input("Enter the ending position (e.g., 'a4'): ")

        start = (int(start[1]) - 1, ord(start[0]) - ord('a'))
        end = (int(end[1]) - 1, ord(end[0]) - ord('a'))

        chess_board.move_piece(start, end)
