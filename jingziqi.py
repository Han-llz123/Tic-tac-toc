'''
Tic-tac-toe      Producer:Commissar Cold Wind
All rights reserved (S)     Open source
'''

import sys, pygame, time

from pygame.constants import MOUSEBUTTONDOWN

pygame.init()
size = width, height = 1080, 1000
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
left, top, bianchang = 200, 200, 200
model = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
isGameover = False
isStart = False
turn = 1    
winner = 0        
# ---------------------------------
# 1 represents party A's turn
# 2 represents party B's turn.
# ---------------------------------

def paint():
    '''
    This function is used to plot
    '''
    global winner
    myfont = pygame.font.SysFont('Arial', 40)
    # ----------------------------------------
    # This variable is used to set the font
    # ----------------------------------------
    
    screen.fill((255, 255, 255))
    red = 255, 0, 0
    for i in range(0, 4):
        pygame.draw.line(screen, red, (left, top + bianchang * i), 
            (bianchang * 3 + left, top + bianchang * i), 2)
        pygame.draw.line(screen, red, (left + bianchang * i, top),
            (left + bianchang * i, bianchang * 3 + top), 2)
    # ------------------------------
    # The area of the game 
    # required to draw tic-tac-toe
    # ------------------------------
    
    
    for i in range(0, 3):            # <---- Row loop
        for j in range(0, 3):        # <---- Column loop
            if model[i][j] == 1:
                pygame.draw.circle(screen, (0, 0, 0), 
                    (left + j * bianchang + bianchang / 2, top + i * bianchang + bianchang / 2),
                    bianchang / 4, 2)
            elif model[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 0),
                    (left + j * bianchang + bianchang / 4, top + i * bianchang + bianchang / 4,
                    bianchang / 2, bianchang / 2), 2)
            

    if isGameover:
        if winner == 1:
            str = 'Game Over, A wins, thank you for your playing!'
        else:
            str = 'Game Over, B wins, thank you for your playing!'
        screen.blit(myfont.render(str, True, (0, 0, 0)), (195, 150))
    # ------------------------------
    # Type with the font you set
    # ------------------------------

                

def getCell(x, y):
    '''
    This function is used to determine which column and
    row the mouse coordinates are in
    '''
    global turn
    if x < left or y < top or x > left + bianchang * 3 or y > top + bianchang * 3:
        return False
    # --------------------------------
    # Set to prevent someone from
    # pointing out of the game area
    # --------------------------------

    j = (int) ((x - left) / bianchang)
    i = (int) ((y - top) / bianchang)
    if model[i][j] == 0:
        model[i][j] = turn
        return True

    return False


def gameover():
    '''
    This function determines whether the game is over
    '''
    global isGameover, winner, turn
    
    for i in range(0, 3):
        gameover = True
        for j in range(0, 3):
            if model[i][j] != turn:
                gameover = False
        if gameover:
            isGameover = True
            winner = turn
            return True
    # ------------------------------
    # Judge whether the line wins
    # ------------------------------

    
    for i in range(0, 3):
        gameover = True
        for j in range(0, 3):
            if model[j][i] != turn:
                gameover = False
        if gameover:
            isGameover = True
            winner = turn
            return True
    # ---------------------------------
    # Judge whether the column wins
    # ---------------------------------

    gameover = True
    for i in range(0, 3):
        if model[i][i] != turn:
            gameover = False
    if gameover:
        isGameover = True
        winner = turn
        return True
    # ----------------------------------
    # Determine whether the left
    # diagonal is winning
    # ----------------------------------

    gameover = True
    for i in range(0, 3):
        if model[i][2 - i] != turn:
            gameover = False
    if gameover:
        isGameover = True
        winner = turn
        return True
    # ----------------------------------
    # Determine whether the right
    # diagonal is winning
    # ----------------------------------





def main():
    '''
    Main function that calls all functions
    '''
    global turn
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if getCell(event.pos[0], event.pos[1]):
                        gameover()
                        if turn == 1:
                            turn = 2
                        elif turn == 2:
                            turn = 1

        paint()
        clock.tick_busy_loop(144)
        pygame.display.update()



if __name__ == '__main__':
    main()

        