import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
PADDLE_SPEED = 5
player1_y = (HEIGHT - PADDLE_HEIGHT) // 2
player2_y = (HEIGHT - PADDLE_HEIGHT) // 2

# Ball settings
BALL_SIZE = 15
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
ball_speed_x = 5
ball_speed_y = 5

# Scores
player1_score = 0
player2_score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT:
        player2_y += PADDLE_SPEED

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if (
        (ball_x <= PADDLE_WIDTH and player1_y < ball_y < player1_y + PADDLE_HEIGHT) or
        (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and player2_y < ball_y < player2_y + PADDLE_HEIGHT)
    ):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball_x <= 0:
        player2_score += 1
        ball_x = WIDTH // 2 - BALL_SIZE // 2
        ball_y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x
    elif ball_x >= WIDTH - BALL_SIZE:
        player1_score += 1
        ball_x = WIDTH // 2 - BALL_SIZE // 2
        ball_y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -ball_speed_x

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, (0, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Draw scores
    player1_text = font.render(f"Player 1: {player1_score}", True, WHITE)
    player2_text = font.render(f"Player 2: {player2_score}", True, WHITE)
    screen.blit(player1_text, (50, 50))
    screen.blit(player2_text, (WIDTH - 200, 50))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()