from abc import ABC, abstractmethod
from typing import Tuple

from gamestatemanager import GameStateManager
from gamestatetype import GameStateType

from pygame.surface import Surface

class GameState(ABC):
    gsm:GameStateManager

    def __init__(self, gsm:GameStateManager):
        self.gsm = gsm

    def switch_state(self, type:GameStateType):
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
    def draw(self, surface:Surface, screen_size: Tuple[float, float], delta_time):
        pass
