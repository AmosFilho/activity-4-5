import pygame

pygame.init()

# Color set
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_RED = (255, 0, 0)
xcolor = 0


size = (1100, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Blackout Remake")

# Score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('03  00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (550, 50)

# Create Bricks
brick = []
brick_cord = 0

# Draw Bricks
# Draw Bricks
for j in range(3):
    y_brick = 40 + (j*50)
    line = []
    for i in range(15):
        x_brick = 5 + (i*100)
        if j == 1:
            xcolor = COLOR_GREEN
        elif j == 2:
            xcolor = COLOR_ORANGE
        elif j == 3:
            xcolor = COLOR_RED
        brick_cord = (xcolor, x_brick, y_brick, 90, 40)



# Sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player = pygame.draw.rect(screen, COLOR_BLUE, (600, 550, 100, 40))
player_x = 600
player_move_left = False
player_move_right = False

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 550
ball_y = 300
ball_dx = 5
ball_dy = 5

score = 0
life = 3

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_move_left = True
            if event.key == pygame.K_RIGHT:
                player_move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_move_left = False
            if event.key == pygame.K_RIGHT:
                player_move_right = False

    screen.fill(COLOR_BLACK)
    # ball collision with the walls
    if ball_y < 0:
        ball_dy *= -1
        bounce_sound_effect.play()
    elif ball_y > 600:
        ball_dy *= -1
        life -= 1
        scoring_sound_effect.play()
    elif (ball_x < 0) or (1100 <= ball_x):
        ball_dx *= -1
        bounce_sound_effect.play()

    # ball collision with the player's paddle
    if 540 <= ball_y:
        if player_x + 100 > ball_x > player_x:
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()
    elif player_x < ball_x <= player_x + 100:
        if 540 <= ball_y:
            ball_dy *= -1
            ball_dx *= -1
            bounce_sound_effect.play()

    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    # player left movement
    if player_move_left:
        player_x -= 5
        # player collides with left wall
        if player_x <= 0:
            player_x = 0
        else:
            player_x += 0

    # player right movement
    if player_move_right:
        player_x += 5
        # player collides with right wall
        if player_x >= 1100:
            player_x = 1100
        else:
            player_x += 0

    # update score hud
    score_text = score_font.render(str(life) + '  ' + str(score), True, COLOR_WHITE, COLOR_BLACK)

    # drawing objects
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(score_text, score_text_rect)
    pygame.draw.rect(screen, COLOR_BLUE, (player_x, 550, 100, 40))
    for i in range(9):
        x_brick = 5 + (i * 100)
        brick[i] = pygame.draw.rect(screen, COLOR_GREEN, (x_brick, 80, 90, 40))

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
