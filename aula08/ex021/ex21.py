import pygame

pygame.mixer.init()
pygame.init()

musicMixer = pygame.mixer.music

musicMixer.load('ex21.mp3')
musicMixer.play()

pygame.event.wait()
