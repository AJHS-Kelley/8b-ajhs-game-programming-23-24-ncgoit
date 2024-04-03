# Final project, Nevaeh Copeland, v0.0
import sys, random, pygame

# Inital Screen
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Snake')
background_pixels = pygame.image.load('img/finalProject/background.png').convert()
screen.blit(background_pixels,(0,0))

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if game_active:
        #     if event.type == pygame.MOUSEBUTTONDOWN:

        # if event.type == pygame.KEYDOWN:

    
        # else:
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #         game_active = True
        #         start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(background_pixels,(0,0))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf,score_rect)

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface,snail_rect)

    else:
        screen.fill((0,225,0))

    pygame.display.update()
    clock.tick(60)




resolution = 0 # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

difficulty = int(input("Please choose a difficulty. Enter 1 for Easy or 2 for Normal.\n"))

if difficulty == 1:
    pygame.display.set_caption('Snake -- EASY')
else:
    pygame.display.set_caption('Snake -- Normal')

# CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE
