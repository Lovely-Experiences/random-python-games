import pygame
import time

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0

color_index = 0
colors = ["red", "blue", "pink", "purple", "orange", "yellow"]

pos_array = []

last_pos_clear = time.time()
actions_debounce = time.time()

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.circle(screen, colors[color_index], player_pos, 10)

    if time.time() - last_pos_clear > .3:
        pos_array.pop()
        last_pos_clear = time.time()

    for x in pos_array:
        pygame.draw.circle(screen, colors[color_index], x, 10)

    pos_array.append(player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_c]:
        screen.fill("black")
    if keys[pygame.K_g]:
        if time.time() - actions_debounce > 1:
            color_index = color_index + 1
            if color_index == colors.__len__():
                color_index = 0
            actions_debounce = time.time()

    pygame.display.update()

    dt = clock.tick(1000) / 1000

pygame.quit()
