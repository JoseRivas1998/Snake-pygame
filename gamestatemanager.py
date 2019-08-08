from typing import Tuple

from gamestate import GameState
from playstate import PlayState
from gamestatetype import GameStateType

from pygame.surface import Surface

class GameStateManager:
    current_state: GameState

    def __init__(self, initial_type: GameStateType):
        self.switch_state(initial_type)

    def switch_state(self, type: GameStateType):
        if type == GameStateType.PLAY:
            self.current_state = PlayState(self)

    def step(self, surface:Surface, screen_size: Tuple[float, float], delta_time:float):
        self.current_state.handle_input()
        self.current_state.update(screen_size, delta_time)
        self.current_state.draw(surface, screen_size, delta_time)
