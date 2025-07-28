import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ENEMY_SIZE = 50
ENEMY_SPEED = 3

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Square Game")

clock = pygame.time.Clock()

player_x = WIDTH // 2
player_y = HEIGHT // 2

enemy_x = 100
enemy_y = 100
enemy_dx = ENEMY_SPEED
enemy_dy = ENEMY_SPEED

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))
    player_y = max(0, min(HEIGHT - PLAYER_SIZE, player_y))

    enemy_x += enemy_dx
    enemy_y += enemy_dy

    if enemy_x <= 0 or enemy_x >= WIDTH - ENEMY_SIZE:
        enemy_dx *= -1
    if enemy_y <= 0 or enemy_y >= HEIGHT - ENEMY_SIZE:
        enemy_dy *= -1

    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)

    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        pygame.time.delay(1000)
        running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()