import pygame
from constants import *

class Piece:
    def __init__(self, row, col, color, value):
        self.row = row
        self.col = col
        self.color = color
        self.value = value
        self.canEnPassant = False
        self.isEnPassant = False
        self.hasMoved = False
        self.x = 0
        self.y = 0
        self.EnPassant()

    def calcPos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def setPiece(self, surface, address):
        self.calcPos()
        img = pygame.image.load(address)
        img = pygame.transform.scale(img, PIECE_SIZE)
        rect = img.get_rect()
        rect.center = (self.x, self.y)
        surface.blit(img, rect)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calcPos()
    
    def EnPassant(self):
        if self.value == 1:
            self.canEnPassant = True

    def __repr__(self):
        return str((self.color, self.value))
