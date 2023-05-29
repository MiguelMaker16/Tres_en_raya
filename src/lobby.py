import pygame
import easygui
from setting import size_width, size_height, window
pygame.font.init()
font = pygame.font.Font(None,60)
text_color = (255, 255, 255)
text = ("Modalidad: Local", "Modalidad: Online") 

screen = pygame.display.set_mode(window)
state = "modality"

def modality():
    for i in range(2):
        rect = pygame.Rect(0, i * (size_height/2), size_width, (size_height/2))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if rect.collidepoint(mouse_x, mouse_y):
            line_color = (0, 255, 0)
        else:
            line_color = (255, 255, 255)
        pygame.draw.rect(screen, line_color, rect, width=1)
        #text
        text_screen = font.render(text[i], True, text_color)
        text_area = text_screen.get_rect()
        text_area.center = (size_width/2, (size_height//4) + ((size_height//2) * i))
        screen.blit(text_screen, text_area)

def online():
    ip = easygui.enterbox("Ingrese dirección IP:", title="Dirección IP")    

def game_lobby():
    if state == "modality":
        modality()