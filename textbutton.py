import pygame
# Reference: https://www.youtube.com/watch?v=8SzTzvrWaAA&t=158s
# Reference: https://www.youtube.com/watch?v=G8MYGDf_9ho

pygame.init()
gui_font = pygame.font.SysFont("arialblack", 20)

TOPCOLOR = '#365880'


class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        # self.top_color = '#475F77'
        self.top_color = TOPCOLOR

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        # self.bottom_color = '#354B5E'
        self.bottom_color = '#475F77'
        # text
        self.text_surf = gui_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, surface):

        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(surface, self.bottom_color,
                         self.bottom_rect, border_radius=12)
        pygame.draw.rect(surface, self.top_color,
                         self.top_rect, border_radius=12)
        surface.blit(self.text_surf, self.text_rect)
        if self.check_click():
            return 1
        else:
            return 0

    def check_click(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            # self.top_color = '#D74B4B'
            self.top_color = '#365880'
            if pygame.mouse.get_pressed()[0] and self.pressed == False:
                self.dynamic_elecation = 0
                self.pressed = True
                action = True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            # self.top_color = '#475F77'
            self.top_color = TOPCOLOR
        return action
