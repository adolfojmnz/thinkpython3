class DukeSprite:

    def __init__(self, image, target_posn):
        self.image = image
        self.target_posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count + 1) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0,
                50, self.image.get_height())
        target_surface.blit(self.image, self.target_posn, patch_rect)

    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt """
        (my_x, my_y) = self.target_posn
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = pt
        return ( x >= my_x and x < my_x + my_width and y >= my_y and y < my_y + my_height)


