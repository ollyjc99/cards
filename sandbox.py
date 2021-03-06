import pygame
import random
import time
from cards import *
from misc import *


def setup(win, deck):
    w, h = win.get_size()

    card_width = round(w*.098)
    card_height = round(h*.167)

    for card in deck.cards:
        card.width = card_width
        card.height = card_height


def sandbox(w, h, deck, clock):
    win = pygame.display.set_mode((w, h))
    pygame.display.set_caption('The @')
    win.fill((75, 125, 75))

    setup(win, deck)
    hand = pygame.sprite.Group()
    table = pygame.sprite.Group()
    running = True
    selected_card = None
    try:
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if not selected_card:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if hand:
                                for card in hand:
                                    if card.rect.collidepoint(event.pos):
                                        selected_card = card
                                        break

                            if deck.cards:
                                if deck.rect.collidepoint(event.pos):
                                    selected_card = deck.cards[0]
                                    deck.cards.pop(0)
                                    hand.add(selected_card)
                                    selected_card.rect.center = pygame.mouse.get_pos()

                        elif event.button == 2:
                            pass

                        elif event.button == 3:
                            if hand:
                                for card in hand:
                                    if card.rect.collidepoint(event.pos):
                                        flip(card)
                                        break

                        elif event.button == 4:
                            if hand:
                                for card in hand:
                                    deck.cards.append(card)
                                    hand.remove(0)
                else:
                    selected_card.rect.center = pygame.mouse.get_pos()

                    if event.type == pygame.MOUSEBUTTONUP:
                        if selected_card.rect.colliderect(deck):
                            deck.cards.append(selected_card)
                            selected_card.kill()

                        selected_card = None

            win.fill((75, 125, 75))
            hand.update()
            deck.draw((round(w * .88), round(h * .80)))
            hand.draw(win)
            pygame.display.update()

    except KeyboardInterrupt:
        print(KeyboardInterrupt)

    except pygame.error:
        print(pygame.error)
