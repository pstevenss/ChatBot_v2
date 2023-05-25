import pygame as pg
# pygame setup start --------------------
pg.init()
screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Bubble Buddies")

#load sprite characters
#mainPlayer = pg.image.load('sprite_Images/mainPlayerIdleFront.png')
forestBg = pg.image.load('sprite_Images/forestBg.png')
mainPlayerSide1 = pg.image.load('sprite_Images/MainPlayerSpriteIdle1.png')
mainPlayerSide2 = pg.image.load('sprite_Images/MainPlayerSpriteIdle2.png')
mainPlayerLeftWalk = pg.image.load('sprite_Images/MainPlayerSpriteWalkLeft.png')
mainPlayerRightWalk = pg.image.load('sprite_Images/MainPlayerSpriteWalkRight.png')

running = True
while running:
    #screen.blit(mainPlayer, (100,100))
    screen.blit(forestBg, (0,0))
    screen.blit(mainPlayerSide1, (500, 500))
    screen.blit(mainPlayerLeftWalk, (400, 500))
    screen.blit(mainPlayerRightWalk, (200, 500))
    screen.blit(mainPlayerSide2, (300, 500))


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
    #
    screen.fill("white")
    # pg.draw.circle(screen, "red", player_pos, 40)
    #
    # keys = pg.key.get_pressed()
    # if keys[pg.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pg.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pg.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pg.K_d]:
    #     player_pos.x += 300 * dt
    #
    # dt = clock.tick(60) / 1000
    #
    #
    #
pg.quit()
## pygame setup end --------------------