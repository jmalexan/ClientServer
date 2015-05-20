import sys, pygame
pygame.init()

size = width, height = 1366, 768
speed = [420, 420]
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")

ball = pygame.transform.scale(ball, (50,50))
ball.set_colorkey((255, 255, 255))
ballrect = ball.get_rect()

while 1 != 2 and "Jon is rekt":
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ball, ballrect)
    pygame.display.flip()
