import pygame as pg
pg.init()
clock = pg.time.Clock()
fps = 60
font = pg.font.Font('fonts/Romulus.ttf', 52) #choosing text pack and the font size
font2 = pg.font.Font('fonts/Alagard.ttf', 35)
# add multiple font packs and call it in while loop
screen = pg.display.set_mode([800,500])

run = True
while run:
    clock.tick(fps) #references fps variable for game speed
    screen.fill('orange') #bg color
    my_text = font.render('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', False , 'white') #setting text , making it false for crisper look rather than true, and choosing the color
    my2ndtext = font2.render('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', False, 'black')
    screen.blit(my_text, (50,150)) #blitting text onto window and putting the position on the window
    screen.blit(my2ndtext, (50,130))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        pg.display.flip()
pg.quit()