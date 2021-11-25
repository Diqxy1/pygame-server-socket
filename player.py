import pygame


class Player():

    def __init__(self, x, y, width, height, color):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._rect = (x, y, width, height)
        self._vel = 3
    
    def draw(self, win):
        pygame.draw.rect(win, self._color, self._rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self._x -= self._vel
        if keys[pygame.K_RIGHT]:
            self._x += self._vel
        if keys[pygame.K_UP]:
            self._y -= self._vel
        if keys[pygame.K_DOWN]:
            self._y += self._vel
        
        self.update()

    def update(self):
        self._rect = (self._x, self._y, self._width, self._height)
