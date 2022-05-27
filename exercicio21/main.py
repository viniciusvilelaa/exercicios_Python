#importando biblioteca para reproduzir mp3
import pygame

import pygame

pygame.init()
pygame.mixer.music.load('onlyfans.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()