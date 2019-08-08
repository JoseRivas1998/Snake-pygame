from typing import Tuple

from gamestate import GameState

from pygame.surface import Surface


class PlayState(GameState):
    def init(self):
        pass

    def handle_input(self):
        pass

    def update(self, screen_size: Tuple[float, float], delta_time):
        pass

    def draw(self, surface:Surface, screen_size: Tuple[float, float], delta_time):
        pass