from pairs import *
from bus import bus
from sandbox import sandbox
import pattern_gen
from cards import *


def setup(win):
    suits = ['spades', 'clubs', 'diamonds', 'hearts']
    faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    list_of_cards = [[face, suit] for face in faces for suit in suits]
    temp_deck = [Card(suit, face) for face, suit in random.sample(list_of_cards, 52)]
    return Deck(win, temp_deck)


def main():
    # Generates Cards
    # pattern_gen.main()

    clock = pygame.time.Clock()
    win_width = 1024
    win_height = 768
    win = pygame.display.set_mode((win_width, win_height))
    icon = pygame.image.load('static/img/template/diamonds.png')
    icon.set_colorkey((255, 255, 255))
    pygame.display.set_icon(icon)

    deck = setup(win)

    pairs(1280, 720, deck, clock)
    # bus(1024, 768, deck, 5, clock)
    # sandbox(1024, 768, deck, clock)


if __name__ == '__main__':
    pygame.init()
    main()
