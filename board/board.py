import pieces
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook
import tile

class Board:
    SIZE_X = 8
    SIZE_Y = 8

    def __init__(self):
        self.board = [[tile.Tile() for x in range(Board.SIZE_X)] for y in range(Board.SIZE_Y)]

        print self.board
        self.new_game()

    def new_game(self):
        self.setup_white()
        self.setup_black()

    def setup_white(self):
        self.setup_pieces(pieces.piece.Piece.WHITE)

    def setup_black(self):
        self.setup_pieces(pieces.piece.Piece.BLACK)

    def setup_pieces(self, color):
        y = 0
        if color == pieces.piece.Piece.BLACK:
            y = Board.SIZE_Y - 1

        for x in range(Board.SIZE_X):
            self.board[x][y + color].piece = Pawn(self.board, color)

        self.board[0][y].piece = Rook(self.board, color)
        self.board[7][y].piece = Rook(self.board, color)

        self.board[1][y].piece = Knight(self.board, color)
        self.board[6][y].piece = Knight(self.board, color)

        self.board[2][y].piece = Bishop(self.board, color)
        self.board[5][y].piece = Bishop(self.board, color)

        self.board[3][y].piece = Queen(self.board, color)
        self.board[4][y].piece = King(self.board, color)

    def print_board(self):
        for y in range(Board.SIZE_Y):
            for x in range(Board.SIZE_X):
                if self.board[x][y].piece == None:
                    print "_",
                else:
                    if self.board[x][y].piece.color == pieces.piece.Piece.WHITE:
                        print self.board[x][y].piece.name().upper(),
                    else:
                        print self.board[x][y].piece.name(),
            print