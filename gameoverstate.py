from typing import Tuple

from pygame.surface import Surface
from pygame.font import Font

from gamestate import GameState
from gamestatetype import GameStateType
from input import MyInput
from snake import Snake


class GameOverState(GameState):
    BLACK = (0, 0, 0)
    font_large: Font
    font_medium: Font
    font_small: Font

    def init(self):
        self.font_large = Font("resources/font/prstartk.ttf", 36)
        self.font_medium = Font("resources/font/prstartk.ttf", 24)
        self.font_small = Font("resources/font/prstartk.ttf", 18)

    def handle_input(self):
        if MyInput.key_check_pressed(MyInput.BACK) or MyInput.key_check_pressed(MyInput.START):
            self.switch_state(GameStateType.TITLE)

    def update(self, screen_size: Tuple[float, float], delta_time):
        pass

    def draw(self, surface: Surface, screen_size: Tuple[float, float], delta_time):
        game_over = (screen_size[0] * 0.5, screen_size[1] * 0.25)
        score = (screen_size[0] * 0.5, screen_size[1] * 0.5)
        score_str = "Score: {:04d}".format(Snake.score)
        prompt = (screen_size[0] * 0.5, screen_size[1] * 0.75)
        prompt_str = "Press Start or Back to return to Title"

        Snake.draw__text("Game Over!", game_over, GameOverState.BLACK, self.font_large, surface)
        Snake.draw__text(score_str, score, GameOverState.BLACK, self.font_medium, surface)
        Snake.draw__text(prompt_str, prompt, GameOverState.BLACK, self.font_small, surface)


