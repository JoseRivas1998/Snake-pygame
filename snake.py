from typing import Tuple

from pygame.font import Font
from pygame.surface import Surface


class Snake:
    score: int = 0

    @staticmethod
    def draw__text(text: str, center: Tuple[float, float], color: Tuple[int, int, int], font: Font,
                       surface: Surface):
        text_surface = font.render(text, False, color)
        text_rect = text_surface.get_rect()
        text_rect.center = center
        surface.blit(text_surface, text_rect)
