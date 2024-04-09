# Final project, Nevaeh Copeland, v0.0
import sys, random, pygame

# Inital Screen
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')
background_pixels = pygame.image.load('img/finalProject/backgroundEasy.png').convert()
screen.blit(background_pixels,(0,0))

clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

# Quality
resolution = 0 # 0 = Low Resolution (800, 600), 1 = High Resolution (1920, 1080)

if resolution == 0:
    x = 800
    y = 600
else:
    x = 1920
    y = 1080

pygame.init()

# difficulty = int(input("Please choose a difficulty. Enter 1 for Easy or 2 for Normal.\n"))

# if difficulty == 1:
#     pygame.display.set_caption('Snake -- EASY')
# else:
#     pygame.display.set_caption('Snake -- Normal')

# CREATE AN if / else BLOCK TO SET RESOLUTION BASED ON THE VARIABLE ABOVE


# Intro Screen
# player_stand = pygame.image.load('img/ultimatePygame/player_stand.png').convert_alpha()
# player_stand = pygame.transform.rotozoom(player_stand,0,2)
# player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Snake Game',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to start', False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if game_active:
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
        #             player_gravity = -20

        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
        #             player_gravity = -20
        # else:
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #         game_active = True
        #         snail_rect.left = 800
        #         start_time = int(pygame.time.get_ticks() / 1000)

        # if event.type == obstacle_timer and game_active:
        #     obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))

    if game_active:
        screen.blit(background_pixels,(250,200))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf,score_rect)
        # score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface,snail_rect)

        # Player
        # player_gravity += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300: player_rect.bottom = 300
        # screen.blit(player_surf,player_rect)
        
        #Obstacle movement
    #     obstacle_rect_list = obstacle_movement(obstacle_rect_list)

    #     # collision
    #     if snail_rect.colliderect(player_rect):
    #         game_active = False
    # else:
        screen.fill((0,225,0))
        score_message = test_font.render(f'Your score: {score}', False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)
        
        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message,score_message_rect)

    pygame.display.update()
    clock.tick(60)
