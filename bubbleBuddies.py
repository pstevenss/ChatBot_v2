import pygame as pg
from spriteSheet import SpriteSheetAnimation
from spriteSheetEye import SpriteSheetAnimationEye
from spriteSheetBat import SpriteSheetAnimationBat


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

enemy_sprite_sheet = pg.image.load('sprite_Images/eyeball.png')
enemy_sprite_sheet2 = pg.image.load('sprite_Images/eyeball.png')
enemy_sprite_sheet3 = pg.image.load('sprite_Images/32x32-bat-sprite.png')

enemy_animation = SpriteSheetAnimation(enemy_sprite_sheet, 32, 32, 100)
enemy_animation2 = SpriteSheetAnimationEye(enemy_sprite_sheet2, 32, 32, 100)
enemy_animation3 = SpriteSheetAnimationBat(enemy_sprite_sheet3, 32, 32, 100)


adventRunSprites = []

# Load and scale sprites
#Running sprites
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-00.png'), (55, 39)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-01.png'), (55, 39)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-02.png'), (55, 39)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-03.png'), (55, 39)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-04.png'), (55, 39)))
adventRunSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-run-05.png'), (55, 39)))

# Create flipped versions of the sprites
adventRunSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventRunSprites]
#Jumping Sprites
adventJumpSprites = []

adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-00.png'), (55, 39)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-01.png'), (55, 39)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-02.png'), (55, 39)))
adventJumpSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-jump-03.png'), (55, 39)))

adventJumpSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventJumpSprites]
#Crouching Sprites
#
# adventCrouchSprites = []
# adventCrouchSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-crouch-00.png'), (55, 42)))
# adventCrouchSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-crouch-01.png'), (55, 42)))
# adventCrouchSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-crouch-02.png'), (55, 42)))
# adventCrouchSprites.append(pg.transform.scale(pg.image.load('sprite_Images/adventurer-crouch-03.png'), (55, 42)))
#
# adventCrouchSpritesFlipped = [pg.transform.flip(sprite, True, False) for sprite in adventCrouchSprites]

# SpriteSheetAnimation usage
sprite_sheet = pg.image.load('sprite_Images/eyeball.png')
frame_width = 32
frame_height = 32
frame_duration = 100
animation = SpriteSheetAnimation(sprite_sheet, frame_width, frame_height, frame_duration)

# SpriteSheetAnimationEyeDuplicate usage
sprite_sheet2 = pg.image.load('sprite_Images/eyeball.png')
frame_width = 32
frame_height = 32
frame_duration = 50  # Adjust the frame duration for smoother animation
animation2 = SpriteSheetAnimationEye(sprite_sheet2, frame_width, frame_height, frame_duration)

# SpriteSheetAnimationBat usage
sprite_sheet3 = pg.image.load('sprite_Images/32x32-bat-sprite.png')
frame_width = 32
frame_height = 32
frame_duration = 50  # Adjust the frame duration for smoother animation
animation3 = SpriteSheetAnimationBat(sprite_sheet3, frame_width, frame_height, frame_duration)

isJump = False
jumpCount = 5
left = False
right = False
walkCount = 0

##where the animation and player movement can be modified

def redrawGameWindow():
    global walkCount, isJump

    # Blit the background image
    screen.blit(forestBg, (0, 0))

    # Update the enemy animation(s)
    enemy_animation.update(dt)
    enemy_current_frame = enemy_animation.get_current_frame()
    screen.blit(enemy_current_frame, (545, 565))

    enemy_animation2.update(dt)
    current_frame2 = enemy_animation2.get_current_frame()
    screen.blit(current_frame2, (245, 565))

    enemy_animation3.update(dt)
    current_frame3 = enemy_animation3.get_current_frame()
    screen.blit(current_frame3, (375, 565))



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
    dt = clock.tick(27)  # Limit the frame rate to 60 FPS
    animation.update(dt) #---------------------------------------------
    current_frame = animation.get_current_frame()
    animation2.update(dt)
    current_frame = animation2.get_current_frame()
    animation3.update(dt)
    current_frame = animation3.get_current_frame()


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
