import pygame

class Menu(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        i = pygame.image.load("naruto.png")
        self.image = pygame.transform.scale(i, (int(i.get_width() * scale), int(i.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def drawc(self, surface):
        surface.blit(self.image, self.rect)