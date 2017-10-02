import sys, pygame
pygame.init()
pygame.key.set_repeat (1, 1)
size = width, height = 500, 340             
speed = [0, 0]
black = 0, 0, 0
white = 100, 0, 200
screen = pygame.display.set_mode(size)          #sets the screen(window) size    
pygame.display.set_caption("Bouncing Ball")     #sets the caption in the title bar
background = pygame.Surface(screen.get_size())  #sets the background surface to the size of the screen
background = background.convert()               #converts the native pixel format of the image to SDL's format
background.fill(white)
ball = pygame.image.load("face.png")            #returns a new surface with the image loaded onto it
ball.convert()                                  #converts the native pixel format of the image to SDL's format
ballrect = ball.get_rect()
clock = pygame.time.Clock()
adj_speed = 10

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                speed[1] = -adj_speed
                speed[0] = 0
            elif event.key == pygame.K_LEFT:
                speed[1] = 0
                speed[0] = -adj_speed
            elif event.key == pygame.K_DOWN:
                speed[1] = +adj_speed
                speed[0] = 0
            elif event.key == pygame.K_RIGHT:
                speed[1] = 0
                speed[0] = +adj_speed
            elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            else:
                speed =[0,0]
            ballrect = ballrect.move(speed)

            if ballrect.centerx > width:          #If ball goes too far right, wrap
                ballrect.centerx = 0
            if ballrect.centerx < 0:            #If ball goes too far left, wrap
                ballrect.centerx = width
            if ballrect.centery > height:          #If ball goes too far down, wrap
                ballrect.centery = 0
            if ballrect.centery < 0:
                ballrect.centery = height
            
   # print ballrect
   # break



    screen.blit(background, (0,0))              #draw the background
    screen.blit(ball, ballrect)                 #draw the player
    pygame.display.flip()                       #
