import pygame as pg
# pygame setup start --------------------
pg.init()
window_width, window_height = 1250, 1000
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Bubble Buddies")

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()

pg.quit()
## pygame setup end --------------------