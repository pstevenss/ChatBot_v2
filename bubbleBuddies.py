import pygame as pg
# pygame setup start --------------------
pg.init()
screen_width = 1000
screen_height = 780
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Bubble Buddies")

#load sprite characters
forestBg = pg.image.load('sprite_Images/forestBg.png')
forestBg = pg.transform.scale(forestBg, (screen_width, screen_height))

sprite_sheet_image = pg.image.load('sprite_Images/characters.png').convert_alpha()

black = (0,0,0)
def getImage(sheet, frame, width, height, scale, color):
    image = pg.Surface((width,height)).convert_alpha()
    image.blit(sheet, (0,0), ((frame * width),0, width,height))
    image = pg.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image

frame_0 = getImage(sprite_sheet_image, 0,  27, 27, 3, black)
frame_1 = getImage(sprite_sheet_image, 1,  27, 27, 3, black)
frame_2 = getImage(sprite_sheet_image, 2,  27, 27, 3, black)
frame_3 = getImage(sprite_sheet_image, 3,  27, 27, 3, black)

#create animation list
animate_list = []
animate_steps = 4

#for x in range(animate_steps):


running = True
while running:
    screen.blit(forestBg, (0,0))

#show frame image
    screen.blit(frame_0, (0,0))
    screen.blit(frame_1, (500,0))
    screen.blit(frame_2, (200,0))
    screen.blit(frame_3, (300,0))



    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.update()
    #
    screen.fill("white")
pg.quit()
## pygame setup end --------------------