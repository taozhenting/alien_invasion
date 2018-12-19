import sys
import pygame

def key_event():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("KeyDown_event")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.event(key_event())