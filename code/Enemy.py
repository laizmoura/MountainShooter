#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        self.vertical_speed = 2 # Velocidade vertical
        self.direction = 1

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        self.rect.centery += self.vertical_speed * 2

        if self.rect.bottom >= WIN_HEIGHT:
            self.direction = -1  # Muda a direção para cima

        if self.rect.top <= 0:
            self.direction = 1

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

