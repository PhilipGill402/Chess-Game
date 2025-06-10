from cmath import inf
import pygame
import sys


pygame.init()
window = pygame.display.set_mode([600,600])
INFINITY = float(inf)
clock = pygame.time.Clock()
timer = 0
dt = 0
turn = 1
selected = []
isCheckGoing = False
board = [
[('b',5),('b',4),('b',3),('b',9),('b',INFINITY),('b',3),('b',4),('b',5)],
[('b',1),('b',1),('b',1),('b',1),('b',1),('b',1),('b',1),('b',1)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('w',1),('w',1),('w',1),('w',1),('w',1),('w',1),('w',1),('w',1)],
[('w',5),('w',4),('w',3),('w',9),('w',INFINITY),('w',3),('w',4),('w',5)]
]

altBoard = [
[('b',5),('b',4),('b',3),('b',9),('b',INFINITY),('b',3),('b',4),('b',5)],
[('b',1),('b',1),('b',1),('b',1),('b',1),('b',1),('b',1),('b',1)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0),('n',0)],
[('w',1),('w',1),('w',1),('w',1),('w',1),('w',1),('w',1),('w',1)],
[('w',5),('w',4),('w',3),('w',9),('w',INFINITY),('w',3),('w',4),('w',5)]
]

def setPieces():
    for i in range(8):
        for l in range(8):
            pos = (l*75 + 17.5, i*75 + 17.5)
            piece = board[i][l]
            if piece[0] == 'b':
                color = 'black'
            elif piece[0] == 'w':
                color = 'white'
            else:
                continue

            if piece[1] == 1:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_pawn.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_pawn.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
            elif piece[1] == 3:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_bishop.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_bishop.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
            elif piece[1] == 4:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_knight.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_knight.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
            elif piece[1] == 5:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_rook.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_rook.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
            elif piece[1] == 9:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_queen.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_queen.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
            elif piece[1] == INFINITY:
                if color == 'white':
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_king.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)
                else:
                    location = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\black_king.png")
                    location = pygame.transform.scale(location, (40,40))
                    window.blit(location, pos)

def checkMoves(piece, x, y, isCheckGoing=False):
    moves = []
    if piece[1] == 5:
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
                if k[0][0] == piece[0]:
                    break
                elif k[0][0] == 'w' and piece[0] == 'b':
                    moves.append(k[1])
                    break
                elif k[0][0] == 'b' and piece[0] == 'w':
                    moves.append(k[1])
                    break
                else:
                    moves.append(k[1])
    
    elif piece[1] == 4:
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
            if i[0] <= 7 and i[1] <= 7 and board[i[1]][i[0]][0] != piece[0] and i[0] >= 0 and i[1] >= 0:
                moves.append(i)
        
    elif piece[1] == 3:
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
                    if space[0] == piece[0]:
                        running = False
                    elif space[0] == 'b' and piece[0] == 'w':
                        moves.append((xCoord, yCoord))
                        running = False
                    elif space[0] == 'w' and piece[0] == 'b':
                        moves.append((xCoord, yCoord))
                        running = False
                    else:
                        moves.append((xCoord, yCoord))
                    counter += 1

            running = True
            counter = 1
            l = 1
            k = 1
    
    elif piece[1] == 9:
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
                if k[0][0] == piece[0]:
                    break
                elif k[0][0] == 'w' and piece[0] == 'b':
                    moves.append(k[1])
                    break
                elif k[0][0] == 'b' and piece[0] == 'w':
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
                    if space[0] == piece[0]:
                        running = False
                    elif space[0] == 'b' and piece[0] == 'w':
                        moves.append((xCoord, yCoord))
                        running = False
                    elif space[0] == 'w' and piece[0] == 'b':
                        moves.append((xCoord, yCoord))
                    else:
                        moves.append((xCoord, yCoord))
                    counter += 1

            running = True
            counter = 1
            l = 1
            k = 1
    
    elif piece[1] == INFINITY:
        running = True
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

                if space[0] == piece[0]:
                    pass
                else:
                    moves.append((xCoord, yCoord))
    
    elif piece[1] == 1:
        possibles = []
        if piece[0] == 'w' and y == 6:
            if board[y-1][x][0] != 'w':
                possibles.append((x,y-1))
                possibles.append((x,y-2))
        elif piece[0] == 'b' and y == 1:
            if board[y+1][x][0] != 'b':
                possibles.append((x,y+1))
                possibles.append((x,y+2))
        elif piece[0] == 'w' and y != 6:
            possibles.append((x,y-1))
        elif piece[0] == 'b' and y != 1:
            possibles.append((x,y+1))
        
        if x+1 < 7:
            if piece[0] == 'w' and board[y-1][x+1][0] == 'b':
                possibles.append((x+1, y-1))
            elif piece[0] == 'b' and board[y+1][x+1][0] == 'w':
                possibles.append((x+1,y+1))
        if x-1 > 0:
            if piece[0] == 'w' and board[y-1][x-1][0] == 'b':
                possibles.append((x-1, y-1))
            elif piece[0] == 'b' and board[y+1][x-1][0] == 'w':
                possibles.append((x-1, y+1))

        for i in possibles:
            space = board[i[1]][i[0]]
            if space[0] == 'b' and piece[0] == 'w':
                moves.append(i)
            elif space[0] == 'w' and piece[0] == 'b':
                moves.append(i)
            elif space[0] == 'n':
                moves.append(i)
            
    else:
        moves = []

    if not isCheckGoing:
        moves = checkMoves(piece, x, y, True)
        if isCheck():
            for i in moves:
                altBoard[i[1]][i[0]] = piece
                altBoard[y][x] = ('n', 0)
                if isCheck(altBoard):
                    moves.remove(i)
                if altBoard != board:
                    print('true')

    return moves

def drawBoard():
    window.fill((255,255,255))
    for i in range(8):
        for k in range(8):
            color = (150,72,56)
            if k % 2 == 0 and i % 2 != 0:
                color = (150,28,0)
            elif k % 2 != 0 and i % 2 == 0:
                color = (150,28,0)
            pygame.draw.rect(window, color, pygame.Rect(k*75,i*75,75,75))
    
    setPieces()

def isCheck(board=board):
    if turn % 2 == 0:
        color = 'b'
    elif turn % 2 != 0:
        color = 'w'
    
    for i in range(8):
        for l in range(8):
            piece = board[i][l]
            if piece[0] != color and piece[0] != 'n':
                moves = checkMoves(piece, l, i, True)
                for j in moves:
                    x = j[0]
                    y = j[1]
                    if board[y][x] == (color, INFINITY):
                        print('check')
                        return True
    
    return False


drawBoard()

while True:
    pygame.display.update()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            drawBoard()
            pos = pygame.mouse.get_pos()
            x = pos[0] // 75
            y = pos[1] // 75
            piece = board[y][x]
            selectedPiece = [piece, (x,y)]
            selected.append(selectedPiece)
            if turn % 2 == 0 and piece[0] == 'b':
                moves = checkMoves(piece, x, y)
            elif turn % 2 != 0 and piece[0] == 'w':
                moves = checkMoves(piece, x, y)
            else:
                moves = []
            for i in moves:
                x = (i[0]*75) + 37.5
                y = (i[1]*75) + 37.5
                pygame.draw.circle(window, (0,0,0), (x,y), 10)
            if timer == 0:
                timer = 0.001
            elif timer < 3:
                x = pos[0] // 75
                y = pos[1] // 75
                prevX = selected[-2][1][0]
                prevY = selected[-2][1][1]
                print(selected[-2][0][0], turn)
                if board[prevY][prevX][0] == piece[0]:
                    continue

                if (x,y) in checkMoves(selected[-2][0], prevX, prevY):
                    if turn % 2 == 0 and selected[-2][0][0] == 'b':
                        board[prevY][prevX] = ('n', 0)
                        board[y][x] = selected[-2][0]
                        drawBoard()
                        turn += 1
                        altBoard = board[:]
                    elif turn % 2 != 0 and selected[-2][0][0] == 'w':
                        board[prevY][prevX] = ('n', 0)
                        board[y][x] = selected[-2][0]
                        drawBoard()
                        turn += 1
                        altBoard = board[:]
                    
                timer = 0

    if timer != 0:
        timer += dt
        if timer >= 3:
            timer = 0
    
    dt = clock.tick(30) / 1000
