from abc import ABC, abstractmethod
from typing import Tuple

from pygame.surface import Surface

from gamestatetype import GameStateType


class GameState(ABC):

    def __init__(self, gsm):
        self.gsm = gsm
        self.init()

    def switch_state(self, type: GameStateType):
        self.gsm.switch_state(type)

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass

    @abstractmethod
    def update(self, screen_size: Tuple[float, float], delta_time):
        pass

    @abstractmethod
    def draw(self, surface: Surface, screen_size: Tuple[float, float], delta_time):
        pass
