import pygame
import sys
from Entity import *


BLOCK_SIZE = 4
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0,0,0))
    grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)
    s_per = 0
    num_rounds = 0
    while num_rounds < 1000:
        draw_grid(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if s_per != 1:
            s_per = update_grid(grid)




        pygame.display.update()





def update_grid(grid):

    num_unhappy = grid.get_unhappy()
    grid.move_unhappy()
    satisfaction_percent = 1 - (num_unhappy/(grid.sizeX*grid.sizeY))
    print(satisfaction_percent , "%: are satisfied")
    return satisfaction_percent 

def draw_grid(grid):
    x = 0;
    y = 0;
    for xPos in range(0, WINDOW_WIDTH, grid.block_size):
        for yPos in range(0, WINDOW_HEIGHT, grid.block_size):
            agent = grid.get((x,y))
            rect = pygame.Rect(xPos, yPos, grid.block_size, grid.block_size)
            pygame.draw.rect(SCREEN, agent.get_color(), rect, width=0)
            y += 1
        y = 0
        x += 1
    pygame.display.update()

           

if __name__ == '__main__':
    main()