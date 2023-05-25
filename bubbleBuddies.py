import pygame as pg

# pygame setup start --------------------
pg.init()
screen_width = 928
screen_height = 650
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
vel = 5
x = 0
y = 565
width = 40
height = 60
pg.display.set_caption("Enchanted Grove")


# Load sprite images
forestBg = pg.image.load('sprite_Images/Background.png')
forestBg = pg.transform.scale(forestBg, (screen_width, screen_height))
adventIdle00 = pg.image.load('sprite_Images/adventurer-idle-00.png')

adventRunSprites = []

# Load and scale the original sprites
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-00.png'), (55, 42)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-01.png'), (55, 42)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-02.png'), (55, 42)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-03.png'), (55, 42)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-04.png'), (55, 42)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-05.png'), (55, 42)))

# Create flipped versions of the sprites
adventRunSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventRunSprites]

adventJumpSprites = []

adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-00.png'), (55, 42)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-01.png'), (55, 42)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-02.png'), (55, 42)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-03.png'), (55, 42)))

adventJumpSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventJumpSprites]


isJump = False
jumpCount = 5
left = False
right = False
walkCount = 0

##where the animation and player movement can be modified

def redrawGameWindow():
    global walkCount ,isJump

    # Blit the background image
    screen.blit(forestBg, (0, 0))

    if isJump:  # Check if player is jumping
        sprite_index = walkCount // 3
        if sprite_index < len(adventJumpSprites):
            if left:
                screen.blit(adventJumpSpritesFlipped[sprite_index], (x, y))
            else:
                screen.blit(adventJumpSprites[sprite_index], (x, y))
            walkCount += 1
        else:
            # Reset jump animation
            walkCount = 0
            isJump = False
    elif left:
        sprite_index = walkCount // 3
        if sprite_index < len(adventRunSpritesFlipped):
            screen.blit(adventRunSpritesFlipped[sprite_index], (x, y))
        else:
            walkCount = 0
            sprite_index = walkCount // 3
            screen.blit(adventRunSpritesFlipped[sprite_index], (x, y))
        walkCount += 1
    elif right:
        sprite_index = walkCount // 3
        if sprite_index < len(adventRunSprites):
            screen.blit(adventRunSprites[sprite_index], (x, y))
        else:
            walkCount = 0
            sprite_index = walkCount // 3
            screen.blit(adventRunSprites[sprite_index], (x, y))
        walkCount += 1
    else:
        screen.blit(adventIdle00, (x, y))  # Display idle image when not moving
        walkCount = 0

    pg.display.update()


## main loops
run = True

while run:
    clock.tick(27)

    # Background sprite Forest - dark
    #screen.blit(forestBg, (0, 0))

    # # Show sprite character images
    # screen.blit(adventRun0, (0, 565))
    # screen.blit(adventRun1, (25, 565))
    # screen.blit(adventRun2, (50, 565))
    # screen.blit(adventRun3, (75, 565))
    # screen.blit(adventRun4, (100, 565))
    # screen.blit(adventRun5, (125, 565))
    #

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pg.K_RIGHT] and x < screen_width - vel - width:
        x += vel
        left = False
        right = True

    else:
        left = False
        right = False
        walkCount = 0

    if not (isJump):
        if keys[pg.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -5:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 5
            isJump = False

    redrawGameWindow()

pg.quit()

## pygame setup end --------------------
