import pygame
from board import *
from constants import SQUARE_SIZE

class Game():
    def __init__(self, surface):
        self.surface = surface
        self._init()

    def update(self):
        if self.board.isCheckMate(self.turn):
            print('checkmate')
        if self.board.isStalemate(self.turn):
            print('stalemate')
        #print(self.board.minimax(3, self.turn, True))
        self.board.draw(self.surface)
        self.drawMoves(self.validMoves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = 'w'
        self.validMoves = []
        self.enPassant = (-1,-1)
        self.doEnPassant = False
        self.color = 'n'
        self.wait = False

    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected: 
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.getPiece(row, col)
        if piece.color != 'n' and piece.color == self.turn:
            self.selected = piece
            self.validMoves = self.board.getMoves(piece, self.turn)
            return True
        
        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece.color != self.selected.color and (col+1, row+1) in self.validMoves:
            if self.selected.value == 1:
                if self.selected.color == 'b' and col+1 < 8:
                    if row == 3:
                        if self.board.board[row][col+1].color == 'w' or self.board.board[row][col-1].color == 'w':
                            if self.board.board[row][col+1].value == 1 or self.board.board[row][col-1].value == 1:
                                self.doEnPassant = True 
                                self.enPassant = (col, row)
                                self.color = 'w' 
                elif self.selected.color == 'w' and col+1 < 8:
                    if row == 4:
                        if self.board.board[row][col+1].color == 'b' or self.board.board[row][col-1].color == 'b':
                            if self.board.board[row][col+1].value == 1 or self.board.board[row][col-1].value == 1:
                                self.doEnPassant = True
                                self.enPassant = (col, row)
                                self.color = 'b'
            self.board.move(self.selected, row, col)
            if self.board.castle and self.board.castlePos == (col+1, row+1):
                self.board.move(self.board.rookPiece, self.board.rookPos[1]-1, self.board.rookPos[0]-1)
                self.board.rookPiece.hasMoved = True
                self.board.castle = False
                self.board.castlePos = (-1,-1)
                self.board.rookPiece = None
                self.board.rookPos = (-1,-1)
            self.selected.hasMoved = True
            if self.doEnPassant and self.enPassant == (self.selected.col, self.selected.row+1) or self.enPassant == (self.selected.col, self.selected.row-1) and self.color == 'w' or self.color == 'b' and not self.wait:
                if self.color == 'w':
                    x, y = self.enPassant
                    self.board.board[y][x] = Piece(y, x, 'n', 0)
                    self.enPassant = (-1,-1)
                    self.color = 'n'
                    self.doEnPassant = False
                else:
                    self.wait = True
            elif self.wait == True:
                x, y = self.enPassant
                self.board.board[y][x] = Piece(y, x, 'n', 0)
                self.enPassant = (-1,-1)
                self.color = 'n'
                self.doEnPassant = False
                self.wait = False
            self.changeTurn()

        else:
            return False

        return True
    
    def changeTurn(self):
        self.validMoves = []
        if self.turn == 'w':
            self.turn = 'b'
        else:
            self.turn = 'w'        

    def drawMoves(self, moves):
        for i in moves:
            row, col = i
            pygame.draw.circle(self.surface, (0,0,0), (row*SQUARE_SIZE - SQUARE_SIZE//2, col*SQUARE_SIZE - SQUARE_SIZE//2), 10)

