import pygame 

pygame.init()

while True:

    event = pygame.event.poll()
    if event != pygame.NOEVENT:
        for i in range(500):
            print(event)
