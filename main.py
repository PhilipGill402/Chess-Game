import pygame
import board
from constants import *
from board import *
from game import *
from button import *

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
state = 'game'
pygame.display.set_caption('Chess')

def getPos(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE

    return row, col

def startScreen():
    running = True
    clock = pygame.time.Clock()
    board = Board()
    pygame.font.init()
    
    while running:
        clock.tick(FPS)
        ev = pygame.event.get()
        board.drawBoard(SCREEN)
        text = pygame.font.Font('font.ttf', 75)
        text = text.render('Chess', True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300,100)
        pos = pygame.mouse.get_pos()
        menuFont = pygame.font.Font('font.ttf', 18)
        playFont = pygame.font.Font('font.ttf', 18)
        playImg = pygame.image.load("StartMenu/PlayRect.png")
        playImg = pygame.transform.scale(playImg, (350,50))
        optionsImg = pygame.image.load("StartMenu/OptionsRect.png")
        optionsImg = pygame.transform.scale(optionsImg, (350,50))
        quitImg = pygame.image.load("StartMenu/QuitRect.png")
        quitImg = pygame.transform.scale(quitImg, (350,50))
        kingImg = pygame.image.load("C:\\Users\\pgill\\Documents\\Coding\\Chess\\Pieces\\white_king.png")
        kingImg = pygame.transform.scale(kingImg, (75,75))
        kingRect = kingImg.get_rect()
        kingRect.center = (300,214)
        playOp = Button(playImg, (300,325), 'Play Vs. Opponent', playFont, (0,0,0), (250,250,250))
        playAI = Button(playImg, (300,400), 'Play Vs. Computer', playFont, (0,0,0), (250,250,250))
        options = Button(optionsImg, (300,475), 'Options', menuFont, (0,0,0), (250,250,250))
        quit = Button(quitImg, (300,550), 'Quit', menuFont, (0,0,0), (250,250,250))
        SCREEN.blit(text, textRect)
        SCREEN.blit(kingImg, kingRect)

        for i in [playOp, playAI, options, quit]:
            i.changeColor(pos)
            i.update(SCREEN)

        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if playOp.checkForInput(pos):
                    main()
                elif playAI.checkForInput(pos):
                    mainAI()
                elif quit.checkForInput(pos):
                    running = False
                '''elif options.checkForInput(pos):
                    options()'''

        pygame.display.update()
        
    pygame.quit()


def main():
    running = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)
    gameBoard = Board()


    while running:
        clock.tick(FPS)
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #gameBoard.minimax(3, 'b', True)
                pos = pygame.mouse.get_pos()
                row, col = getPos(pos)                
                piece = gameBoard.board[row][col]
                game.select(row, col)

        game.update()
    
    pygame.quit()

def mainAI():
    pass

startScreen()

#mainAI()

#main()