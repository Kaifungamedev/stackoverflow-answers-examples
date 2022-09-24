import pygame
pygame.init()

screen_width = 800
screen_height = 600

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("key map test")
x = screen_width / 2
y = screen_height / 2
width = 40
height = 60
vel = 5

run = True

class key_map():
    
    def Left():
        if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            return True

    def Right():
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            return True

    def Up():
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
            return True

    def Down():
        if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
            return True


while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if key_map().Left():
        x -= vel

    if key_map().Right():
        x += vel

    if key_map().Up():
        y -= vel
    if key_map().Down():
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
