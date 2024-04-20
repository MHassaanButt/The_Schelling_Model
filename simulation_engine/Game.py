import pygame
import sys
from Entity import *


BLOCK_SIZE = 20
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0,0,0))
    grid = Grid(WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)

    while True:
        draw_grid(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                update_grid(grid)




        pygame.display.update()





def update_grid(grid):
    grid.swap((0,0),grid.find_free_space())

def draw_grid(grid):
    x = 0;
    y = 0;
    for xPos in range(0, grid.sizeX, grid.block_size):
        for yPos in range(0, grid.sizeY, grid.block_size):
            agent = grid.get((x,y))
            rect = pygame.Rect(xPos, yPos, grid.block_size, grid.block_size)
            pygame.draw.rect(SCREEN, agent.get_color(), rect, width=0)
            y += 1
        y = 0
        x += 1

           

if __name__ == '__main__':
    main()