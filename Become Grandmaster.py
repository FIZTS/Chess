class ChessPiece:
    def __init__(self, color): #attribute
        self.color = color

    def __str__(self): #class representation
        return self.symbol

    def valid_moves(self, start, end, board):
        raise NotImplementedError("Some chess pieces are not implemented a valid move method")


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
        #return row_start == row_end or col_start == col_end
    
        is_horizontal = row_start == row_end
        is_vertical = col_start == col_end

        if is_horizontal:
            # Obstracle checking Horizon
            step_col = 1 if col_end > col_start else -1
            j = col_start + step_col
            while j != col_end:
                if board[row_start][j] is not None:
                    return False
                j += step_col
        elif is_vertical:
            # Obstracle checking Vertical
            step_row = 1 if row_end > row_start else -1
            i = row_start + step_row
            while i != row_end:
                if board[i][col_start] is not None:
                    return False
                i += step_row

        return True


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

        row_diff = abs(row_end - row_start)
        col_diff = abs(col_end - col_start)

        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = board[row_end][col_end]
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
            # Got blocked
            step_row = 1 if row_end > row_start else -1
            step_col = 1 if col_end > col_start else -1

            i, j = row_start + step_row, col_start + step_col
            while i != row_end and j != col_end:
                if board[i][j] is not None:
                    return False  # Got blocked
                i += step_row
                j += step_col

            target_piece = board[row_end][col_end]
            # Check piece colour
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

    def valid_moves(self, start, end, board):
        row_start, col_start = start
        row_end, col_end = end

        is_horizontal = row_start == row_end
        is_vertical = col_start == col_end
        is_diagonal = abs(row_end - row_start) == abs(col_end - col_start)

        # Check if it is blocked
        if is_horizontal:
            step_col = 1 if col_end > col_start else -1
            j = col_start + step_col
            while j != col_end:
                if board[row_start][j] is not None:
                    return False  # Got blocked
                j += step_col
        elif is_vertical:
            step_row = 1 if row_end > row_start else -1
            i = row_start + step_row
            while i != row_end:
                if board[i][col_start] is not None:
                    return False  # Got blocked
                i += step_row
        elif is_diagonal:
            step_row = 1 if row_end > row_start else -1
            step_col = 1 if col_end > col_start else -1
            i, j = row_start + step_row, col_start + step_col
            while i != row_end and j != col_end:
                if board[i][j] is not None:
                    return False  # Got blocked
                i += step_row
                j += step_col
        else:
            return False  # Invalid move

        target_piece = board[row_end][col_end]
        
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
            # Check if it is None or Opponent's piece
            if target_piece is None or target_piece.color != self.color:
                return True

        return False


class ChessBoard:
    def __init__(self):
        self.board = [[None] * 8 for _ in range(8)]
        self.current_player = 'white'
        
    def switch_turn(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

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
        print("   a  b  c  d  e  f  g  h")
        for i, row in enumerate(self.board, 1):
            print(f"{i}", end="")
            for piece in row:
                if piece is None:
                    print(' . ', end='')
                else:
                    print(piece, end='')
            print(f" {i}")

    def is_valid_move(self, start, end):
        if any(coord < 0 or coord >= 8 for coord in start + end):
            return False
        if start == end or self.board[start[0]][start[1]] is None:
            return False

        piece = self.board[start[0]][start[1]]

        if piece.color != self.current_player:
            raise ValueError(f"It's {self.current_player.capitalize()}'s turn. Cannot move {piece.color}'s piece.")

        return piece.valid_moves(start, end, self.board)

    def move_piece(self, start, end):
        try:
            if self.is_valid_move(start, end):
                self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
                self.board[start[0]][start[1]] = None
                self.switch_turn()

                # Check if either king is gone
                white_king_exists = any(isinstance(piece, King) and piece.color == 'white' for row in self.board for piece in row)
                black_king_exists = any(isinstance(piece, King) and piece.color == 'black' for row in self.board for piece in row)

                if not white_king_exists or not black_king_exists:
                    print("                        ♥")
                    print("!!!!!!!!!!!!!!!!!!!!Game Over!!!!!!!!!!!!!!!!!!!!")
                    print("                        ♥")
                    exit()

        except ValueError as e:
            print(f"Invalid move: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.initialize_board()
    while True:
        chess_board.print_board()
        start_input = input(f"{chess_board.current_player.capitalize()}'s turn. Enter the starting position (e.g., 'a2'): ")
        end_input = input(f"{chess_board.current_player.capitalize()}'s turn. Enter the ending position (e.g., 'a4'): ")

        if len(start_input) != 2 or len(end_input) != 2:
            print("Invalid input format. Please enter positions in the format 'a2'.")
            continue

        try:
            start = (int(start_input[1]) - 1, ord(start_input[0]) - ord('a'))
            end = (int(end_input[1]) - 1, ord(end_input[0]) - ord('a'))
        except ValueError:
            print("Invalid input values. Please enter valid positions.")
            continue

        chess_board.move_piece(start, end)

'''
นะโม ตัสสะ ภะคะวะโต อะระหะโต สัมมาสัมพุทธัสสะ
'''