import random

from entity import Entity
from vector2 import Vector2


class Food(Entity):
    def __init__(self, grid_size: int, head_pos: Vector2):
        super().__init__()
        self.reset(grid_size, head_pos)

    def reset(self, grid_size:int, head_pos: Vector2):
        x = head_pos.x
        y = head_pos.y
        while x == head_pos.x and y == head_pos.y:
            x = random.randint(0, grid_size - 1)
            y = random.randint(0, grid_size - 1)
        self.pos.x = x
        self.pos.y = y
