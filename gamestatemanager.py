from typing import Tuple

from pygame.surface import Surface

from gamestate import GameState
from gamestatetype import GameStateType
from playstate import PlayState
from gameoverstate import GameOverState
from titlestate import TitleState


class GameStateManager:
    current_state: GameState
    should_exit: bool

    def __init__(self, initial_type: GameStateType):
        self.switch_state(initial_type)
        self.should_exit = False

    def switch_state(self, type: GameStateType):
        if type == GameStateType.PLAY:
            self.current_state = PlayState(self)
        if type == GameStateType.GAME_OVER:
            self.current_state = GameOverState(self)
        if type == GameStateType.TITLE:
            self.current_state = TitleState(self)

    def step(self, surface: Surface, screen_size: Tuple[float, float], delta_time: float):
        self.current_state.handle_input()
        self.current_state.update(screen_size, delta_time)
        self.current_state.draw(surface, screen_size, delta_time)

    def exit(self):
        self.should_exit = True
