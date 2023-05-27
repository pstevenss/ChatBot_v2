import pygame as pg
pg.init()
clock = pg.time.Clock()
fps = 60
font = pg.font.Font('Romulus.ttf', 52) #choosing text pack
screen = pg.display.set_mode([800,500])

run = True
while run:
    clock.tick(fps) #references fps variable for game speed
    screen.fill('orange') #bg color
    my_text = font.render('check out this text', True, 'white') #setting text , making it true, and choosing the color
    screen.blit(my_text, (100,150)) #blitting text onto window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        pg.display.flip()
pg.quit()