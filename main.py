from deck import Deck
from hand import *

deck = Deck() 
deck.shuffle()
stack = deck.draw_stack(5)

deck.show_stack(stack)

# High Card
high_card = is_high_card(stack)
print(f'High card: {high_card}')

if is_one_pair(stack):
    print("para")