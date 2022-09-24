import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
rect = pygame.Rect(0, 0, 40, 60)
rect.center = win.get_rect().center
vel = 5

class KeyMap():
    def __init__(self):
        self.keys = pygame.key.get_pressed()
    def left(self):
        return self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]
    def right(self):
        return self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]
    def down(self):
        return self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]
    def up(self):
        return self.keys[pygame.K_UP] or self.keys[pygame.K_w]

run = True
while run:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key_map = KeyMap()
    rect.x += (key_map.right() - key_map.left()) * vel
    rect.y += (key_map.down() - key_map.up()) * vel

    win.fill((0, 0, 0)) 
    pygame.draw.rect(win, (255, 0, 0), rect)
    pygame.display.update()

pygame.quit()