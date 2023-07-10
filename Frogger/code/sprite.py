import pygame

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups) -> None:
        super().__init__(groups)
        self.image = surf 
        #pos is the top left, position we get from parameters
        self.rect = self.image.get_rect(topleft = pos)
        #to change th height and shape
        self.hitbox = self.rect.inflate(0, -self.rect.height/2) #to make it relative
class LongSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height/2)
        self.hitbox.bottom = self.rect.bottom -10 #sub 10 pixels from th bottom of th sprite rect
