import pygame
import os
import sys

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
FPS = 60


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    play_sprites = pygame.sprite.Group()
    exit_sprites = pygame.sprite.Group()
    fon = pygame.transform.scale(load_image('startscreen.jpg'), (1920, 1080))
    screen.blit(fon, (0, 0))
    playbut = pygame.sprite.Sprite()
    playbut.image = load_image('play.png')
    playbut.rect = playbut.image.get_rect()
    playbut.rect.x = 650
    playbut.rect.y = 480
    play_sprites.add(playbut)
    exitbut = pygame.sprite.Sprite()
    exitbut.image = load_image('exit.png')
    exitbut.rect = exitbut.image.get_rect()
    exitbut.rect.x = 650
    exitbut.rect.y = 700
    exit_sprites.add(exitbut)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and playbut.rect.collidepoint(event.pos):
                pass
            if event.type == pygame.MOUSEBUTTONDOWN and exitbut.rect.collidepoint(event.pos):
                terminate()
        play_sprites.draw(screen)
        exit_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


start_screen()