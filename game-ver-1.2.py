import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SIZE = 50
PLAYER_SPEED = 5

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Square Game with Obstacles")

clock = pygame.time.Clock()

player_rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)

obstacles = [
    pygame.Rect(200, 150, 100, 300),
    pygame.Rect(500, 100, 50, 400),
    pygame.Rect(300, 450, 200, 30)
]

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    move_x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * PLAYER_SPEED
    move_y = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * PLAYER_SPEED

    new_rect = player_rect.move(move_x, 0)
    if not any(new_rect.colliderect(obstacle) for obstacle in obstacles):
        player_rect.x += move_x

    new_rect = player_rect.move(0, move_y)
    if not any(new_rect.colliderect(obstacle) for obstacle in obstacles):
        player_rect.y += move_y

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()