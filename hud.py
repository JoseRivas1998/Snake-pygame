from typing import Tuple

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface


class HUD:
    font: Font
    score: Surface
    score_rect: Rect

    def __init__(self):
        self.font = Font("resources/font/prstartk.ttf", 24)

    def draw(self, surface: Surface, start_x: float, start_y: float, grid_width: float, score: int, font_color: Tuple[int, int, int]):
        self.score = self.font.render("Score: {:04d}".format(score), False, font_color)
        self.score_rect = self.score.get_rect()
        center_x = (grid_width * 0.5) + start_x
        center_y = start_y - 10 - (self.score_rect.height * 0.5)
        self.score_rect.center = (center_x, center_y)
        surface.blit(self.score, self.score_rect)
