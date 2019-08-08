from abc import ABC
from typing import Tuple

from pygame.surface import Surface

from direction import Direction
from rectangle import Rectangle
from vector2 import Vector2


class Entity(ABC):
    pos: Vector2
    dir: Direction

    def __init__(self):
        self.pos = Vector2()
        self.dir = Direction.NONE

    def colliding_with(self, e):
        """

        :type e: Entity
        """
        return self.pos.x == e.pos.x and self.pos.y == e.pos.y

    def draw(self, surface: Surface, color: Tuple[int, int, int], start_x: float, start_y: float, width: float, height: float):
        Rectangle(start_x + self.pos.x * width, start_y + self.pos.y * height, width, height).display(surface, color)

    def move_in_direction(self):
        if self.dir == Direction.UP:
            self.pos.y -= 1
        if self.dir == Direction.DOWN:
            self.pos.y += 1
        if self.dir == Direction.LEFT:
            self.pos.x -= 1
        if self.dir == Direction.RIGHT:
            self.pos.x += 1
