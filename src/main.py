import pygame, sys
from lobby import game_lobby
pygame.init()

#setting game
pygame.display.set_caption("Tres En Raya")
clock = pygame.time.Clock()
#state game
state = "lobby"

while True:
    #State Game
    if state == "lobby":
        game_lobby()
    elif state == "local":
        game_local()
    elif state == "Online":
        game_online()
    #End game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
    clock.tick(60) 