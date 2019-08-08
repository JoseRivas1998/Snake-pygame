from typing import Tuple

import pygame
from pygame.surface import Surface
from gamestatemanager import GameStateManager
from gamestatetype import GameStateType
from input import MyInput, MyInputProcessor

# CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class App:
    size: Tuple[float, float]
    running: bool
    window_title: str
    screen: Surface
    font: pygame.font.Font
    last_time: float
    delta_time: float
    gsm: GameStateManager

    def __init__(self, width, height, title):
        self.size = (width, height)
        self.running = False
        self.window_title = title

    def begin(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.window_title)
        self.gsm = GameStateManager(GameStateType.TITLE)
        self.last_time = 0
        self.running = True
        self.game_loop()

    def poll_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                MyInputProcessor.key_down(event.key)
            if event.type == pygame.KEYUP:
                MyInputProcessor.key_up(event.key)
        pass

    def step(self):
        self.screen.fill((0xD2, 0xD2, 0xD2))
        self.poll_event()
        self.gsm.step(self.screen, self.size, self.delta_time)
        MyInput.update()
        pygame.display.flip()
        if self.gsm.should_exit:
            self.exit()

    def calculate_delta_time(self):
        current_time = pygame.time.get_ticks()
        self.delta_time = (current_time - self.last_time) / 1000.0
        self.last_time = current_time

    def game_loop(self):
        while self.running:
            self.calculate_delta_time()
            self.step()

    def exit(self):
        self.running = False
