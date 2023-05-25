import pygame as pg
# pygame setup start --------------------
pg.init()
screen_width = 1000
screen_height = 780
sprite_width = 350
sprite_height = 500
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Bubble Buddies")

#load sprite characters
#mainPlayer = pg.image.load('sprite_Images/mainPlayerIdleFront.png')
forestBg = pg.image.load('sprite_Images/forestBg.png')
forestBg = pg.transform.scale(forestBg, (screen_width, screen_height))

mainPlayerSide1 = pg.image.load('sprite_Images/MainPlayerSpriteIdle1.png')
mainPlayerSide1 = pg.transform.scale(mainPlayerSide1, (sprite_width, sprite_height))

mainPlayerSide2 = pg.image.load('sprite_Images/MainPlayerSpriteIdle2.png')
mainPlayerSide2 = pg.transform.scale(mainPlayerSide2, (sprite_width, sprite_height))

mainPlayerLeftWalk = pg.image.load('sprite_Images/MainPlayerSpriteWalkLeft.png')
mainPlayerLeftWalk = pg.transform.scale(mainPlayerLeftWalk, (sprite_width, sprite_height))

mainPlayerRightWalk = pg.image.load('sprite_Images/MainPlayerSpriteWalkRight.png')
mainPlayerRightWalk = pg.transform.scale(mainPlayerRightWalk, (sprite_width, sprite_height))


running = True
while running:
    #screen.blit(mainPlayer, (100,100))
    screen.blit(forestBg, (0,0))
    screen.blit(mainPlayerSide1, (25,350))
    screen.blit(mainPlayerLeftWalk, (75,350))
    screen.blit(mainPlayerSide2, (200,350))
    screen.blit(mainPlayerRightWalk, (80,350))
# fix the position with sprite blitting

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