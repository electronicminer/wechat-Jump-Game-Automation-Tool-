import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
TANK_SIZE = 50
BULLET_SIZE = 10
ENEMY_TANK_SIZE = TANK_SIZE

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Tank(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed

class Bullet(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.speed = 5

    def move(self):
        self.y -= self.speed

class EnemyTank(Tank):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_TANK_SIZE, ENEMY_TANK_SIZE)

# Create a player tank
player_tank = Tank(100, 100, TANK_SIZE, TANK_SIZE)

# Create an enemy tank
enemy_tank = EnemyTank(WIDTH - 150, HEIGHT - 150, ENEMY_TANK_SIZE, ENEMY_TANK_SIZE)

# Create a list to hold bullets
bullets = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the player tank based on which arrow key is held down
    if keys[pygame.K_LEFT]:
        player_tank.move(-1, 0)
    if keys[pygame.K_RIGHT]:
        player_tank.move(1, 0)
    if keys[pygame.K_UP]:
        player_tank.move(0, -1)
    if keys[pygame.K_DOWN]:
        player_tank.move(0, 1)

    # Prevent the tank from moving off the screen
    player_tank.x = max(0, min(player_tank.x, WIDTH - TANK_SIZE))
    player_tank.y = max(0, min(player_tank.y, HEIGHT - TANK_SIZE))

    # Create a new bullet if the space bar is held down and no bullets currently exist
    if keys[pygame.K_SPACE] and not bullets:
        bullets.append(Bullet(player_tank.x + (TANK_SIZE / 2), player_tank.y + (TANK_SIZE / 2)))

    # Move all existing bullets
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0 or bullet.y > HEIGHT:
            bullets.remove(bullet)

    # Check for collisions between the player tank and any bullets
    for bullet in bullets[:]:
        if bullet.colliderect(player_tank):
            bullets.remove(bullet)
            print("Game Over")

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, player_tank)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    pygame.draw.rect(screen, (128, 64, 0), enemy_tank)

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // 60)