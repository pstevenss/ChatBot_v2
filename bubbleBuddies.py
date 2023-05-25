import pygame as pg

# pygame setup start --------------------
pg.init()
screen_width = 928
screen_height = 650
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
vel = 5
x = 55
y = 22
width = 40
height = 60
pg.display.set_caption("Bubble Buddies")

# Load sprite characters
forestBg = pg.image.load('sprite_Images/Background.png')
forestBg = pg.transform.scale(forestBg, (screen_width, screen_height))

adventIdle00 = pg.image.load('sprite_Images/adventurer-idle-00.png')
adventIdle00 = pg.transform.scale(adventIdle00, (55, 42))
adventIdle01 = pg.image.load('sprite_Images/adventurer-idle-01.png')
adventIdle01 = pg.transform.scale(adventIdle01, (55, 42))
adventIdle02 = pg.image.load('sprite_Images/adventurer-idle-02.png')
adventIdle02 = pg.transform.scale(adventIdle02, (55, 42))
adventIdle03 = pg.image.load('sprite_Images/adventurer-idle-03.png')
adventIdle03 = pg.transform.scale(adventIdle03, (55, 42))

isJump = False
jumpCount = 5

run = True

while run:
    pg.time.delay(50)

    # Background sprite Forest - dark
    screen.blit(forestBg, (0, 0))

    # Show sprite character images
    screen.blit(adventIdle00, (0, 565))
    screen.blit(adventIdle01, (25, 565))
    screen.blit(adventIdle02, (50, 565))
    screen.blit(adventIdle03, (75, 565))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel

    if keys[pg.K_RIGHT] and x < screen_width - vel - width:
        x += vel

    if not isJump:
        if keys[pg.K_UP] and y > vel:
            y -= vel

        if keys[pg.K_DOWN] and y < screen_height - height - vel:
            y += vel

        if keys[pg.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -5:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 5
            isJump = False

    screen.fill((0, 0, 0))
    pg.display.update()

pg.quit()

## pygame setup end --------------------
