import pygame
from time import sleep
import long_responses as long

# get simple pygame running for demo
# pygame should open after X amount of seconds when user says they want to play

# possible 3 game choices for user to choose from, for now 1 to get demo working

def runningGame():
    print(long.R_CONFIRM)
    sleep(2)
    print("Opening game in..")
    sleep(3)
    print("3...")
    sleep(2)
    print("2..")
    sleep(1)
    print("1.")

runningGame()


## copied the code for demo purposes to have game open,to be changed
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

