class SpriteSheetAnimationBat:
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
        if self.frame_width > sheet_width or self.frame_height > sheet_height:
            raise ValueError("Frame dimensions exceed sprite sheet size")
        for y in range(0, sheet_height, self.frame_height):
            if y + self.frame_height > sheet_height:
                break  # Skip incomplete row at the bottom of the sprite sheet
            for x in range(0, sheet_width, self.frame_width):
                if x + self.frame_width > sheet_width:
                    break  # Skip incomplete frame at the end of the row
                frame = self.sprite_sheet.subsurface((x, y, self.frame_width, self.frame_height))
                frames.append(frame)
        return frames

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.frame_duration:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % self.frame_count

    def get_current_frame(self):
        return self.frames[self.current_frame]
