from typing import Tuple

from pygame.surface import Surface
from pygame.font import Font

from gamestate import GameState
from gamestatetype import GameStateType
from input import MyInput
from snake import Snake


class TitleState(GameState):
    BLACK = (0, 0, 0)
    font_large: Font
    font_small: Font

    def init(self):
        self.font_large = Font("resources/font/prstartk.ttf", 48)
        self.font_small = Font("resources/font/prstartk.ttf", 18)

    def handle_input(self):
        if MyInput.key_check_pressed(MyInput.BACK):
            self.gsm.exit()
        if MyInput.key_check_pressed(MyInput.START):
            self.switch_state(GameStateType.PLAY)
        pass

    def update(self, screen_size: Tuple[float, float], delta_time):
        pass

    def draw(self, surface: Surface, screen_size: Tuple[float, float], delta_time):
        title = (screen_size[0] * 0.5, screen_size[1] * 0.25)
        prompt = (screen_size[0] * 0.5, screen_size[1] * 0.75)

        Snake.draw__text("Snake", title, TitleState.BLACK, self.font_large, surface)
        Snake.draw__text("Press Start to Play, Exit to Quit", prompt, TitleState.BLACK, self.font_small, surface)
