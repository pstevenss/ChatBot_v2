import pygame as pg
pg.init()
clock = pg.time.Clock()
fps = 60
font = pg.font.Font('fonts/Romulus.ttf', 52) #choosing text pack and the font size
# add multiple font packs and call it in while loop
screen = pg.display.set_mode([800,500])

run = True
while run:
    clock.tick(fps) #references fps variable for game speed
    screen.fill('orange') #bg color
    my_text = font.render('check out this text', False , 'white') #setting text , making it false for crisper look rather than true, and choosing the color
    screen.blit(my_text, (100,150)) #blitting text onto window and putting the position on the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        pg.display.flip()
pg.quit()