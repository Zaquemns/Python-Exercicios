import pygame

pygame.init()
gtav = 'gta-v-theme.mp3'
pygame.mixer.music.load(gtav)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass

