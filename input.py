from typing import List
import pygame


class MyInput:
    keys: List[bool] = []
    pkeys: List[bool] = []
    NUM_KEYS = 6
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    START = 4
    BACK = 5
    for i in range(NUM_KEYS):
        keys.append(False)
        pkeys.append(False)

    @classmethod
    def update(cls):
        for i in range(cls.NUM_KEYS):
            cls.pkeys[i] = cls.keys[i]

    @classmethod
    def set_key(cls, key: int, b: bool):
        cls.keys[key] = b

    @classmethod
    def key_check(cls, key: int):
        return cls.keys[key]

    @classmethod
    def key_check_pressed(cls, key: int):
        return cls.keys[key] and not cls.pkeys[key]


class MyInputProcessor:
    @staticmethod
    def key_down(key_code: int):
        MyInputProcessor.__key_event__(key_code, True)

    @staticmethod
    def key_up(key_code: int):
        MyInputProcessor.__key_event__(key_code, False)

    @staticmethod
    def __key_event__(key_code: int, value: bool):
        if key_code == pygame.K_UP or key_code == pygame.K_w:
            MyInput.set_key(MyInput.UP, value)
        if key_code == pygame.K_DOWN or key_code == pygame.K_s:
            MyInput.set_key(MyInput.DOWN, value)
        if key_code == pygame.K_LEFT or key_code == pygame.K_a:
            MyInput.set_key(MyInput.LEFT, value)
        if key_code == pygame.K_RIGHT or key_code == pygame.K_d:
            MyInput.set_key(MyInput.RIGHT, value)
        if key_code == pygame.K_RETURN:
            MyInput.set_key(MyInput.START, value)
        if key_code == pygame.K_ESCAPE:
            MyInput.set_key(MyInput.BACK, value)
