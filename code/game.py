#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Define o tamanho da tela do jogo / CTRL+ALT+L organiza

    def run(self):



        while True:
            menu = Menu(self.window)
            menu.run()

            # Check for all events
            #for event in pygame.event.get():
                #if event.type == pygame.QUIT:
                    #pygame.quit()  # Close Window/Fechar Janela
                    #quit()  # end pygame
