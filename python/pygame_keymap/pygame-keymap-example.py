import pygame
pygame.init()

screen_width = 800
screen_height = 600
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("key map test")
clock = pygame.time.Clock()
FPS = 60
x = screen_width / 2
y = screen_height / 2
width = 40
height = 60
vel = 5

run = True

class KeyMap():
    def __init__(self):
        self.keys = pygame.key.get_pressed()
    def Left(self):
        return self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]
    def Right(self):
        return self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]
    def Down(self):
        return self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]
    def Up(self):
        return self.keys[pygame.K_UP] or self.keys[pygame.K_w]
#thanks to Rabbid76 from stack overflow for helping me clearing a bug

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if KeyMap().Left():
        x -= vel

    if KeyMap().Right():
        x += vel

    if KeyMap().Up():
        y -= vel
    if KeyMap().Down():
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
