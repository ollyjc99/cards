import pygame
import random
from PIL import Image
from collections import namedtuple
from pairs import *
from bus import bus
from sandbox import sandbox
import pattern_gen


class Card(object):
    def __init__(self, win, width, height, suit, face):
        self.win = win
        self.x = 0; self.y = 0
        self.width = width
        self.height = height
        self.suit = suit
        self.face = face
        self.flipped = False
        self.im = self.flip()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def set_rect(self):
        self.x -= round(self.width / 2)
        self.y -= round(self.height / 2)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x + round(self.width // 2), self.y + round(self.height // 2))

    def draw(self, pos=None):
        if pos:
            self.x, self.y = pos
            self.rect.center = (self.x + round(self.width // 2), self.y + round(self.height // 2))
            self.win.blit(self.im, self.rect)
            self.win.blit(pygame.transform.scale(self.im, (self.width, self.height)), pos)

    def move(self, pos):
        self.x, self.y = pos
        self.rect = self.im.get_rect()
        self.rect.center = (pos)
        self.win.blit(self.im, self.rect)

    def flip(self):
        if self.flipped:
            return pygame.image.load(f'static/img/{self.suit}/{self.face}.png')
        else:
            return pygame.image.load('static/img/template/card_back.png')

    def check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())


class Deck(object):
    def __init__(self, deck):
        self.deck = deck


def main():
    # Generates Cards
    # pattern_gen.main()
    clock = pygame.time.Clock()
    win_width = 1024
    win_height = 768
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_icon(pygame.image.load('static/img/template/diamonds.png'))

    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [[face, suit] for face in faces for suit in suits]

    # pairs(1280, 720, Card, deck, clock)
    # bus(1024, 768, Card, deck, 5, clock)
    sandbox(1024, 768, Card, deck, clock)


if __name__ == '__main__':
    pygame.init()
    main()
