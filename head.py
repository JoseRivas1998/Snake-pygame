import random
from typing import List

import pygame

from direction import Direction
from entity import Entity
from input import MyInput

class Head(Entity):
    input_queue: List[Direction]

    def __init__(self, grid_size: int):
        super().__init__()
        direction_int = random.randint(0, 3)
        if direction_int == 0:
            self.dir = Direction.UP
        elif direction_int == 1:
            self.dir = Direction.DOWN
        elif direction_int == 2:
            self.dir = Direction.LEFT
        elif direction_int == 3:
            self.dir = Direction.RIGHT
        self.pos.x = int(grid_size / 2)
        self.pos.y = int(grid_size / 2)
        self.input_queue = []

    def __peek_queue__(self):
        if len(self.input_queue) > 0:
            return self.input_queue[0]
        else:
            return Direction.NONE

    def __pop_queue__(self):
        if len(self.input_queue) > 0:
            dir = self.input_queue[0]
            del self.input_queue[0]
            return dir
        else:
            return Direction.NONE

    def __push_queue__(self, dir: Direction):
        self.input_queue.append(dir)

    def __queue_empty__(self):
        return len(self.input_queue) == 0

    def handle_input(self):
        input_queue_size = len(self.input_queue)
        input_queue_peek = self.__peek_queue__()
        if MyInput.key_check_pressed(MyInput.UP):
            if (input_queue_size == 0 and self.dir != Direction.DOWN) or (
                    input_queue_size > 0 and input_queue_peek != Direction.DOWN):
                self.__push_queue__(Direction.UP)
        if MyInput.key_check_pressed(MyInput.DOWN):
            if (input_queue_size == 0 and self.dir != Direction.UP) or (
                    input_queue_size > 0 and input_queue_peek != Direction.UP):
                self.__push_queue__(Direction.DOWN)
        if MyInput.key_check_pressed(MyInput.RIGHT):
            if (input_queue_size == 0 and self.dir != Direction.LEFT) or (
                    input_queue_size > 0 and input_queue_peek != Direction.LEFT):
                self.__push_queue__(Direction.RIGHT)
        if MyInput.key_check_pressed(MyInput.LEFT):
            if (input_queue_size == 0 and self.dir != Direction.RIGHT) or (
                    input_queue_size > 0 and input_queue_peek != Direction.RIGHT):
                self.__push_queue__(Direction.LEFT)

    def update(self):
        if not self.__queue_empty__():
            self.dir = self.__pop_queue__()
        self.move_in_direction()
