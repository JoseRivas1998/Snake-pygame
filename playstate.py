from typing import Tuple, List

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from body import Body
from food import Food
from gamestate import GameState
from gamestatetype import GameStateType
from head import Head
from hud import HUD
from input import MyInput
from snake import Snake


class PlayState(GameState):
    TICK_LENGTH: float = 0.1
    GRID_SIZE: int = 50
    INITIAL_BODY_SIZE = 3
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    FOOD_COLOR = (0xFF, 0x90, 0x00)

    tick_time: float
    head: Head
    body: List[Body]
    food: Food
    hud: HUD

    def init(self):
        PlayState.TICK_LENGTH = 0.1
        self.tick_time = 0
        self.head = Head(PlayState.GRID_SIZE)
        self.body = []
        for i in range(PlayState.INITIAL_BODY_SIZE):
            self.__add_body__()
        self.food = Food(PlayState.GRID_SIZE, self.head.pos)
        self.hud = HUD()
        pass

    def handle_input(self):
        if MyInput.key_check_pressed(MyInput.BACK):
            self.switch_state(GameStateType.TITLE)
        self.head.handle_input()
        pass

    def update(self, screen_size: Tuple[float, float], delta_time):
        self.tick_time += delta_time
        if self.tick_time >= PlayState.TICK_LENGTH:
            self.tick_time = 0
            self.__tick__(delta_time)
        pass

    def __tick__(self, delta_time):
        for body in self.body:
            if body.colliding_with(self.head):
                Snake.score = len(self.body) - PlayState.INITIAL_BODY_SIZE
                self.switch_state(GameStateType.GAME_OVER)
        if len(self.body) >= 1:
            self.body[0].set_direction(self.head)
            for i in range(1, len(self.body)):
                self.body[i].set_direction(self.body[i - 1])
            for body in self.body:
                body.update()
        self.head.update()
        if self.head.colliding_with(self.food):
            PlayState.TICK_LENGTH *= .95
            self.food.reset(PlayState.GRID_SIZE, self.head.pos)
            self.__add_body__()
        if self.head.pos.x < 0 or self.head.pos.x > PlayState.GRID_SIZE - 1 or self.head.pos.y < 0 or self.head.pos.y > PlayState.GRID_SIZE - 1:
            Snake.score = len(self.body) - PlayState.INITIAL_BODY_SIZE
            self.switch_state(GameStateType.GAME_OVER)

    def draw(self, surface: Surface, screen_size: Tuple[float, float], delta_time):
        cell_width = 10
        grid_width = cell_width * PlayState.GRID_SIZE
        start_x = (screen_size[0] * 0.5) - (grid_width * 0.5)
        start_y = (screen_size[1] * 0.5) - (grid_width * 0.5)

        pygame.draw.rect(surface, PlayState.WHITE, Rect(start_x, start_y, grid_width, grid_width), 1)

        self.head.draw(surface, PlayState.BLACK, start_x, start_y, cell_width, cell_width)
        for body in self.body:
            body.draw(surface, PlayState.BLACK, start_x, start_y, cell_width, cell_width)

        self.food.draw(surface, PlayState.FOOD_COLOR, start_x, start_y, cell_width, cell_width)
        score = len(self.body) - PlayState.INITIAL_BODY_SIZE
        self.hud.draw(surface, start_x, start_y, grid_width, score, PlayState.BLACK)

    def __add_body__(self):
        if len(self.body) < 1:
            self.body.append(Body(self.head))
        else:
            self.body.append(Body(self.body[len(self.body) - 1]))
