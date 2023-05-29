import pygame, sys
from sprites import Board, Circle, Eks
from type_sprite import addCircle, addEks
from winner import playerWinner
pygame.init()

#Settings
window = (640,480)
pygame.display.set_caption("Tres En Raya")
clock = pygame.time.Clock()
fps = 60
screen = pygame.display.set_mode(window)
screen_data = pygame.display.Info()
screen_width = screen_data.current_w
screen_height = screen_data.current_h
start = False
#board
grid_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]   
]
#print(grid_board[1][1]) = 5
#Sprites
sprite_list = pygame.sprite.Group()
type_sprite = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        else:
            mouse_down = False
    #Draw board
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for row in range(3):
        for col in range(3):
            rect = pygame.Rect(col * screen_width//3, row * screen_height//3, screen_width//3, screen_height//3)
            #change color rect
            if rect.collidepoint(mouse_x, mouse_y):
                line_color = (0, 255, 0)
            else:
                line_color = (255, 255, 255)
            #actions
            if grid_board[row][col] == 0 and rect.collidepoint(mouse_x, mouse_y) and mouse_down:
                mouse_down = False
                if type_sprite == 1:
                    sprite_list.add(addCircle(rect.x, rect.y))
                    #type_sprite *= -1
                else:
                    sprite_list.add(addEks(rect.x, rect.y))
                grid_board[row][col] = type_sprite
                type_sprite *= -1
                #analisis por consola
                for grid in grid_board:
                    for value in grid:
                        print("{:2d}".format(value), end=" ")
                    print()
                        
            pygame.draw.rect(screen, line_color, rect, width=1)
    #Draw Sprites
    sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(fps)   