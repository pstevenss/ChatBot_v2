import pygame as pg

class SpriteSheetAnimation:
    def __init__(self, sprite_sheet, frame_width, frame_height, frame_duration):
        self.sprite_sheet = sprite_sheet
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_duration = frame_duration
        self.frames = self.load_frames()
        self.current_frame = 0
        self.frame_count = len(self.frames)
        self.timer = 0

    def load_frames(self):
        frames = []
        sheet_width, sheet_height = self.sprite_sheet.get_size()
        for y in range(0, sheet_height, self.frame_height):
            for x in range(0, sheet_width, self.frame_width):
                frame = self.sprite_sheet.subsurface(pg.Rect(x, y, self.frame_width, self.frame_height))
                frames.append(frame)
        return frames

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % self.frame_count

    def get_current_frame(self):
        return self.frames[self.current_frame]

# Example usage
pg.init()
screen = pg.display.set_mode((400, 400))
clock = pg.time.Clock()

# Load sprite sheet
sprite_sheet = pg.image.load('sprite_Images/eyeball.png')

# Define frame dimensions and duration
frame_width = 55
frame_height = 42
frame_duration = 100  # Time in milliseconds between frame updates

# Create sprite sheet animation
animation = SpriteSheetAnimation(sprite_sheet, frame_width, frame_height, frame_duration)

running = True
while running:
    dt = clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    animation.update(dt)

    screen.fill((255, 255, 255))  # Clear the screen
    current_frame = animation.get_current_frame()
    screen.blit(current_frame, (100, 100))  # Blit the current frame onto the screen

    pg.display.flip()  # Update the display

pg.quit()
