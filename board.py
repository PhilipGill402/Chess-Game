from constants import *
import pygame
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.altBoard = []
        self.createBoard()
        self.copyBoard(self.board)
        self.castle = False
        self.castlePos = (-1,-1)
        self.rookPos = (-1,-1)
        self.rookPiece = None
    
    def promote(self):
        pass

    def drawBoard(self, surface):
        surface.fill((255,255,255))
        for i in range(8):
            for k in range(8):
                color = (150,72,56)
                if k % 2 == 0 and i % 2 != 0:
                    color = (150,28,0)
                elif k % 2 != 0 and i % 2 == 0:
                    color = (150,28,0)
                pygame.draw.rect(surface, color, pygame.Rect(k*75,i*75,75,75))
    
    def createBoard(self):
        for row in range(ROWS):
            self.board.append([])
            self.altBoard.append([])
            for col in range(COLS):
                if row == 0 and col == 0 or row == 0 and col == 7:
                    self.board[row].append(Piece(row, col, 'b', 5))
                elif row == 0 and col == 1 or row == 0 and col == 6:
                    self.board[row].append(Piece(row, col, 'b', 4))
                elif row == 0 and col == 2 or row == 0 and col == 5:
                    self.board[row].append(Piece(row, col, 'b', 3))
                elif row == 0 and col == 3:
                    self.board[row].append(Piece(row, col, 'b', 9))
                elif row == 0 and col == 4:
                    self.board[row].append(Piece(row, col, 'b', 1000))
                elif row == 1:
                    self.board[row].append(Piece(row, col, 'b', 1))
                elif row > 1 and row < 6:
                    self.board[row].append(Piece(row, col, 'n', 0))
                elif row == 6:
                    self.board[row].append(Piece(row, col, 'w', 1))
                elif row == 7 and col == 0 or row == 7 and col == 7:
                    self.board[row].append(Piece(row, col, 'w', 5))
                elif row == 7 and col == 1 or row == 7 and col == 6:
                    self.board[row].append(Piece(row, col, 'w', 4))
                elif row == 7 and col == 2 or row == 7 and col == 5:
                    self.board[row].append(Piece(row, col, 'w', 3))
                elif row == 7 and col == 3:
                    self.board[row].append(Piece(row, col, 'w', 9))
                elif row == 7 and col == 4:
                    self.board[row].append(Piece(row, col, 'w', 1000))
    
    def copyBoard(self, board):
        self.altBoard = []
        counter = 0
        for i in board:
            self.altBoard.append([])
            for l in i:
                self.altBoard[counter].append(l)
            counter += 1

    def draw(self, surface):
        self.drawBoard(surface)
        for row in range(0,ROWS):
            for col in range(0,COLS):
                piece = self.board[row][col]
                if piece.color != 'n':
                    strPiece = str(piece)
                    if strPiece == str(('b', 1)):
                        address = "Pieces/black_pawn.png"
                    elif strPiece == str(('b', 3)):
                        address = "Pieces/black_bishop.png"
                    elif strPiece == str(('b', 4)):
                        address = "Pieces/black_knight.png"
                    elif strPiece == str(('b', 5)):
                        address = "Pieces/black_rook.png"
                    elif strPiece == str(('b', 9)):
                        address = "Pieces/black_queen.png"
                    elif strPiece == str(('b', 1000)):
                        address = "Pieces/black_king.png"
                    elif strPiece == str(('w', 1)):
                        address = "Pieces/white_pawn.png"
                    elif strPiece == str(('w', 3)):
                        address = "Pieces/white_bishop.png"
                    elif strPiece == str(('w', 4)):
                        address = "Pieces/white_knight.png"
                    elif strPiece == str(('w', 5)):
                        address = "Pieces/white_rook.png"
                    elif strPiece == str(('w', 9)):
                        address = "Pieces/white_queen.png"
                    elif strPiece == str(('w', 1000)):
                        address = "Pieces/white_king.png"
                    
                    piece.setPiece(surface, address)

    def move(self, piece, row, col):
        isThereEnPassant = self.isThereEnPassant()
        if isThereEnPassant[0]:
            isThereEnPassant[1].canEnPassant = False
        
        self.board[row][col] = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = Piece(piece.row, piece.col, 'n', 0)
        piece.move(row, col)

        if row == 7 and str(piece) == ('b', 1):
            self.promote()
        if row == 0 and str(piece) == ('w', 1):
            self.promote()
    
    def moveAlt(self, piece, row, col):
        self.altBoard[row][col] = self.altBoard[piece.row][piece.col]
        self.altBoard[piece.row][piece.col] = Piece(piece.row, piece.col, 'n', 0)
    
    def getPiece(self, row, col):
        return self.board[row][col]

    def getMoves(self, piece, turn):
        moves = []
        refinedMoves = []
        x = piece.col
        y = piece.row
        board = self.board
        isEnPassant = False
        enPassant = (-1,-1)

        if piece.value == 5:
            horizontal = []
            vertical = []
            left = []
            right = []
            up = []
            down = []
            isLeft = True
            isUp = True
            counter = 0
            for i in board[y]:
                horizontal.append([i, (counter, y)])
                counter += 1
            counter = 0
            for i in board:
                move = [i[x], (x, counter)]
                vertical.append(move)
                counter += 1
            for i in horizontal:
                if i[0] == piece:
                    isLeft = False
                elif isLeft:
                    left.append(i)
                elif not isLeft:
                    right.append(i)
            for i in vertical:
                if i[0] == piece:
                    isUp = False
                elif isUp:
                    up.append(i)
                elif not isUp:
                    down.append(i)

            left.reverse()
            up.reverse()
            allMoves = [left, right, up, down]
            for i in allMoves:
                for k in i:
                    k[1] = (k[1][0] + 1, k[1][1] + 1)
                    if k[0].color == piece.color:
                        break
                    elif k[0].color == 'w' and piece.color == 'b':
                        moves.append(k[1])
                        break
                    elif k[0].color == 'b' and piece.color == 'w':
                        moves.append(k[1])
                        break
                    else:
                        moves.append(k[1])
        
        elif piece.value == 4:
            possibles = []
            for i in range(1,9):
                if i == 1:
                    move = (x + 1, y + 2)
                    possibles.append(move)
                elif i == 2:
                    move = (x + 2, y + 1)
                    possibles.append(move)
                elif i == 3:
                    move = (x + 2, y - 1)
                    possibles.append(move)
                elif i == 4:
                    move = (x + 1, y - 2)
                    possibles.append(move)
                elif i == 5:
                    move = (x - 1, y - 2)
                    possibles.append(move)
                elif i == 6:
                    move = (x - 2, y - 1)
                    possibles.append(move)
                elif i == 7:
                    move = (x - 2, y + 1)
                    possibles.append(move)
                elif i == 8:
                    move = (x - 1, y + 2)
                    possibles.append(move)
                
            for i in possibles:
                if i[0] <= 7 and i[1] <= 7 and board[i[1]][i[0]].color != piece.color and i[0] >= 0 and i[1] >= 0:
                    x = i[0] + 1
                    y = i[1] + 1
                    moves.append((x,y))
            
        elif piece.value == 3:
            possibles = []
            l = 1
            k = 1
            running = True
            counter = 1

            for i in range(1,5):

                if i % 2 == 0:
                    l = -1
                if i > 2:
                    k = -1
                
                while running:
                    xCoord = (counter * l) + x
                    yCoord = (counter * k) + y
                    if xCoord > 7 or xCoord < 0 or yCoord > 7 or yCoord < 0:
                        running = False
                    else:
                        space = board[yCoord][xCoord]
                        if space.color == piece.color:
                            running = False
                        elif space.color == 'b' and piece.color == 'w':
                            moves.append((xCoord+1, yCoord+1))
                            running = False
                        elif space.color == 'w' and piece.color == 'b':
                            moves.append((xCoord+1, yCoord+1))
                            running = False
                        else:
                            moves.append((xCoord+1, yCoord+1))
                        counter += 1

                running = True
                counter = 1
                l = 1
                k = 1
        
        elif piece.value == 9:
            horizontal = []
            vertical = []
            left = []
            right = []
            up = []
            down = []
            isLeft = True
            isUp = True
            counter = 0
            for i in board[y]:
                horizontal.append([i, (counter, y)])
                counter += 1
            counter = 0
            for i in board:
                move = [i[x], (x, counter)]
                vertical.append(move)
                counter += 1
            for i in horizontal:
                if i[0] == piece:
                    isLeft = False
                elif isLeft:
                    left.append(i)
                elif not isLeft:
                    right.append(i)
            for i in vertical:
                if i[0] == piece:
                    isUp = False
                elif isUp:
                    up.append(i)
                elif not isUp:
                    down.append(i)

            left.reverse()
            up.reverse()
            allMoves = [left, right, up, down]

            for i in allMoves:
                for k in i:
                    k[1] = (k[1][0] + 1, k[1][1] + 1)
                    if k[0].color == piece.color:
                        break
                    elif k[0].color == 'w' and piece.color == 'b':
                        moves.append(k[1])
                        break
                    elif k[0].color == 'b' and piece.color == 'w':
                        moves.append(k[1])
                        break
                    else:
                        moves.append(k[1])
            possibles = []
            l = 1
            k = 1
            running = True
            counter = 1

            for i in range(1,5):

                if i % 2 == 0:
                    l = -1
                if i > 2:
                    k = -1
                
                while running:
                    xCoord = (counter * l) + x
                    yCoord = (counter * k) + y
                    if xCoord > 7 or xCoord < 0 or yCoord > 7 or yCoord < 0:
                        running = False
                    else:
                        space = board[yCoord][xCoord]
                        if space.color == piece.color:
                            running = False
                        elif space.color == 'b' and piece.color == 'w':
                            moves.append((xCoord+1, yCoord+1))
                            running = False
                        elif space.color == 'w' and piece.color == 'b':
                            moves.append((xCoord+1, yCoord+1))
                        else:
                            moves.append((xCoord+1, yCoord+1))
                        counter += 1

                running = True
                counter = 1
                l = 1
                k = 1
        
        elif piece.value == 1000:
            isLeft = True
            left = []
            right = []
            for i in range(1,9):
                if i < 4:
                    l = 1
                elif i < 6:
                    l = 0
                else:
                    l = -1
                if i in [1, 4, 6]:
                    k = -1
                elif i in [2, 7]:
                    k = 0
                else:
                    k = 1
                
                xCoord = x+k
                yCoord = y+l
                if xCoord > 7 or xCoord < 0 or yCoord > 7 or yCoord < 0:
                    pass
                else:
                    space = board[yCoord][xCoord]

                    if space.color == piece.color:
                        pass
                    else:
                        moves.append((xCoord+1, yCoord+1))
            
            for i in board[y]:
                if isLeft:
                    left.append(i)
                else:
                    right.append(i)
                if i.value == 1000:
                    isLeft = False

            if not piece.hasMoved:
                rook = left[0]
                if rook.value == 5 and not rook.hasMoved and left[1].value == 0 and left[2].value == 0 and left[3].value == 0:
                    if piece.color == 'b':
                        y = 0
                        color = 'b'
                    else:
                        y = 7
                        color = 'w'
                    canCastle = True
                    for i in range(3):
                        if i == 0:
                            x = 4
                        elif i == 1:
                            x = 3
                        elif i == 2:
                            x = 2
                        if self.getRayCast(self.board, x, y, color):
                            canCastle = False
                    if canCastle:
                        moves.append((3,y+1))
                        self.castlePos = (3,y+1)
                        self.rookPos = (4,y+1)
                        self.rookPiece = self.board[y][0]
                        self.castle = True


                rook = right[-1]
                if rook.value == 5 and not rook.hasMoved and right[0].value == 0 and right[1].value == 0 and not piece.hasMoved:
                    if piece.color == 'b':
                        y = 0
                        color = 'b'
                    else:
                        y = 7
                        color = 'w'
                    canCastle = True
                    for i in range(3):
                        if i == 0:
                            x = 4
                        elif i == 1:
                            x = 5
                        elif i == 2:
                            x = 6
                        if self.getRayCast(self.board, x, y, color):
                            canCastle = False
                            break
                    if canCastle:
                        moves.append((7,y+1))
                        self.castlePos = (7,y+1)
                        self.rookPos = (6, y+1)
                        self.rookPiece = self.board[y][7]
                        self.castle = True
      
        elif piece.value == 1:
            possibles = []
            if piece.color == 'w' and y == 6:
                if board[y-1][x].value == 0:
                    possibles.append((x+1,y))
                    possibles.append((x+1,y-1))
            elif piece.color == 'b' and y == 1:
                if board[y+1][x].value == 0:
                    possibles.append((x+1,y+2))
                    possibles.append((x+1,y+3))
            elif piece.color == 'w' and y != 6:
                possibles.append((x+1,y))
            elif piece.color == 'b' and y != 1:
                possibles.append((x+1,y+2))
            
            if piece.color == 'w' and y == 3 and piece.canEnPassant and x > 0 and x < 7:
                if board[y][x-1].color == 'b' and board[y][x-1].value == 1:
                    possibles.append((x, y))
                    piece.isEnPassant = True
                elif board[y][x+1].color == 'b' and board[y][x+1].value == 1:
                    possibles.append((x+2,y))
                    piece.isEnPassant = True
            elif piece.color == 'b' and y == 4 and piece.canEnPassant and x > 0 and x < 7:
                if board[y][x+1].color == 'w' and board[y][x+1].value == 1:
                    possibles.append((x+2,y+2))
                    piece.isEnPassant = True
                elif board[y][x-1].color == 'w' and board[y][x-1].value == 1:
                    possibles.append((x,y+2))
                    piece.isEnPassant = True

            if x+1 < 8:
                if piece.color == 'w' and board[y-1][x+1].color == 'b':
                    possibles.append((x+2, y))
                elif piece.color == 'b' and board[y+1][x+1].color == 'w':
                    possibles.append((x+2,y+2))
            if x+1 > 1:
                if piece.color == 'w' and board[y-1][x-1].color == 'b':
                    possibles.append((x, y))
                elif piece.color == 'b' and board[y+1][x-1].color == 'w':
                    possibles.append((x, y+2))
            
            for i in possibles:
                space = board[i[1]-1][i[0]-1]
                if space.color == 'b' and piece.color == 'w':
                    if y-1 == i[1]-1:
                        if x+1 == i[0]-1 or x-1 == i[0]-1:
                            moves.append(i)
                elif space.color == 'w' and piece.color == 'b':
                    if y+1 == i[1]-1:
                        if x+1 == i[0]-1 or x-1 == i[0]-1:
                            moves.append(i)
                elif space.color == 'n':
                    moves.append(i)
                
        else:
            moves = []
        
        for i in moves:
            self.moveAlt(piece, i[1]-1, i[0]-1)
            if not self.isCheck(self.altBoard, turn):
                refinedMoves.append(i)
            self.copyBoard(board)

        moves = refinedMoves[:]

        return moves

    def isCheck(self, board, turn):
        for i in board:
            for l in i:
                if l.color == turn and l.value == 1000:
                    x = i.index(l)
                    y = board.index(i)

        if self.getRayCast(board, x, y):
            return True
        
        else:
            return False

    def getRayCast(self, board, x, y, color=None):
        piece = board[y][x]
        if color == None:
            color = piece.color
        horizontal = []
        vertical = []
        left = []
        right = []
        up = []
        down = []
        isLeft = True
        isUp = True
        counter = 0
        for i in board[y]:
            horizontal.append([i, (counter, y)])
            counter += 1
        counter = 0
        for i in board:
            move = [i[x], (x, counter)]
            vertical.append(move)
            counter += 1
        for i in horizontal:
            if i[0] == piece:
                isLeft = False
            elif isLeft:
                left.append(i)
            elif not isLeft:
                right.append(i)
        for i in vertical:
            if i[0] == piece:
                isUp = False
            elif isUp:
                up.append(i)
            elif not isUp:
                down.append(i)

        left.reverse()
        up.reverse()
        allMoves = [left, right, up, down]
        for i in allMoves:
            for k in i:
                k[1] = (k[1][0] + 1, k[1][1] + 1)
                if k[0].color == color:
                    break
                elif k[0].color == 'w' and color == 'b':
                    if k[0].value == 5 or k[0].value == 9:
                        return True
                    
                elif k[0].color == 'b' and color == 'w':
                    if k[0].value == 5 or k[0].value == 9:
                        return True
                        
        possibles = []
        for i in range(1,9):
            if i == 1:
                move = (x + 1, y + 2)
                possibles.append(move)
            elif i == 2:
                move = (x + 2, y + 1)
                possibles.append(move)
            elif i == 3:
                move = (x + 2, y - 1)
                possibles.append(move)
            elif i == 4:
                move = (x + 1, y - 2)
                possibles.append(move)
            elif i == 5:
                move = (x - 1, y - 2)
                possibles.append(move)
            elif i == 6:
                move = (x - 2, y - 1)
                possibles.append(move)
            elif i == 7:
                move = (x - 2, y + 1)
                possibles.append(move)
            elif i == 8:
                move = (x - 1, y + 2)
                possibles.append(move)
                
        for i in possibles:
            if i[0] <= 7 and i[1] <= 7 and board[i[1]][i[0]].color != color and i[0] >= 0 and i[1] >= 0 and board[i[1]][i[0]].color != 'n' and board[i[1]][i[0]].value == 4:
                return True
        
        possibles = []
        l = 1
        k = 1
        running = True
        counter = 1

        for i in range(1,5):

            if i % 2 == 0:
                l = -1
            if i > 2:
                k = -1
                
            while running:
                xCoord = (counter * l) + x
                yCoord = (counter * k) + y
                if xCoord > 7 or xCoord < 0 or yCoord > 7 or yCoord < 0:
                    running = False
                else:
                    space = board[yCoord][xCoord]
                    if space.color == color:
                        running = False
                    elif space.color == 'b' and color == 'w':
                        if space.value == 3 or space.value == 9:
                            running = False
                            return True
                        else:
                            running = False

                    elif space.color == 'w' and color == 'b':
                        if space.value == 3 or space.value == 9:
                            running = False
                            return True
                        else:
                            running = False
                            
                    counter += 1

            running = True
            counter = 1
            l = 1
            k = 1

        if y+1 < 8 and x+1 < 8 and color == 'b' and board[y+1][x+1].color == 'w' and board[y+1][x+1].value == 1:
                return True
        if y-1 > 0 and x+1 < 8:
            if color == 'w' and board[y-1][x+1].color == 'b' and board[y-1][x+1].value == 1:
                return True
        if y+1 < 8 and x-1 > 0:
            if color == 'b' and board[y+1][x-1].color == 'w' and board[y+1][x-1].value == 1:
                return True
        if y-1 > 0 and x-1 > 0:
            if color == 'w' and board[y-1][x-1].color == 'b' and board[y-1][x-1].value == 1:
                return True
        
        possibles = []
        for i in range(1,9):
            if i < 4:
                l = 1
            elif i < 6:
                l = 0
            else:
                l = -1
            if i in [1, 4, 6]:
                k = -1
            elif i in [2, 7]:
                k = 0
            else:
                k = 1
                
            xCoord = x+k
            yCoord = y+l
            if xCoord > 7 or xCoord < 0 or yCoord > 7 or yCoord < 0:
                pass
            else:
                space = board[yCoord][xCoord]

                if space.color == color:
                    pass
                elif space.color == 'w' and color == 'b' and space.value == 1000:
                    return True
                elif space.color == 'b' and color == 'w' and space.value == 1000:
                    return True
                else:
                    pass
        
        return False

    def isThereEnPassant(self):
        for i in range(0,8):
            for l in range(0,8):
                piece = self.board[i][l]
                y = i
                x = l
                if piece.value == 1 and x < 7 and x > 0:
                    if piece.color == 'w' and y == 3 and piece.canEnPassant:
                        if self.board[y][x-1].color == 'b' and self.board[y][x-1].value == 1:
                            piece.isEnPassant = True
                            return (True, piece)
                        elif self.board[y][x+1].color == 'b' and self.board[y][x+1].value == 1:
                            piece.isEnPassant = True
                            return (True, piece)
                    elif piece.color == 'b' and y == 4 and piece.canEnPassant:
                        if self.board[y][x+1].color == 'w' and self.board[y][x+1].value == 1:
                            piece.isEnPassant = True
                            return (True, piece)
                        elif self.board[y][x-1].color == 'w' and self.board[y][x-1].value == 1:
                            piece.isEnPassant = True
                            return (True, piece)

        
        return (False, None)

    def isCheckMate(self, color):
        isCheckMate = True
        for i in range(8):
            for l in range(8):
                piece = self.board[i][l]
                if piece.color == 'n' or piece.color != color:
                    continue
                else:
                    moves = self.getMoves(piece, color)
                    for j in moves:
                        self.moveAlt(piece, j[1]-1, j[0]-1)
                        if not self.isCheck(self.altBoard, color):
                            isCheckMate = False
                        self.copyBoard(self.board)
        
        
        if isCheckMate:
            return True
        else:
            return False

    def eval(self):
        eval = 0
        for i in self.board:
            for piece in i:
                if piece.color == 'b':
                    eval -= piece.value
                elif piece.color == 'w':
                    eval += piece.value
        
        return eval

    def minimax(self, depth, turn, maxPlayer):
        if depth == 0 or self.isCheckMate(turn):
            return self.eval()

        elif turn == 'w' and maxPlayer == True or turn == 'b' and maxPlayer == False:
            maxEval = -1000000
            for i in range(8):
                for l in range(8):
                    moves = self.getMoves(self.board[i][l], turn)
                    for j in moves:
                        self.moveAlt(self.board[i][l], j[1]-1, j[0]-1)
                        if turn == 'w':
                            turn = 'b'
                        else:
                            turn = 'w'
                        eval = self.minimax(depth-1, turn, False)
                        maxEval = max(maxEval, eval)
            return maxEval
        
        else:
            minEval = 1000000
            for i in range(8):
                for l in range(8):
                    moves = self.getMoves(self.board[i][l], turn)
                    for j in moves:
                        self.moveAlt(self.board[i][l], j[1]-1, j[0]-1)
                        if turn == 'w':
                            turn = 'b'
                        else:
                            turn = 'w'
                        eval = self.minimax(depth-1, turn, True)
                        minEval = min(minEval, eval)
            return minEval

    def isStalemate(self, color):
        isStalemate = True
        for i in range(8):
            for l in range(8):
                piece = self.board[i][l]
                if piece.color != color:
                    continue
                else:
                    moves = self.getMoves(piece, color)
                    if len(moves) > 0:
                        isStalemate = False
        
        
        if isStalemate:
            return True
        else:
            return False