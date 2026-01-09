from deck import Deck
from hand import *

deck = Deck() 
deck.shuffle()
stack = deck.draw_stack(5)

# deck.show_stack(stack)
print()

# Funckja pokazująca jaki jest wynik rozgrywki
def check_the_hand(stack):
    if (is_Quads(stack)):
        return "QUADS!"
    elif (is_full_house(stack)):
        return "FULL HOUSE!"
    elif (is_flush(stack)):
        return "FLUSH"
    elif (is_strit(stack)):
        return "STRIT"
    elif (is_three_of_kind(stack)):
        return "THREE OF A KIND!"
    elif (are_two_pairs(stack)):
        return "TWO PAIRS!"
    elif (is_one_pair(stack)):
        return "PAIR!"
    else: return is_high_card(stack)

# print(check_the_hand(stack))

def check_how_many_attemps(deck):
    result = ""
    attempts = 0
    while result != "FLUSH":
        deck.reset()
        stack = deck.draw_stack(5)
        result = check_the_hand(stack)
        attempts += 1
    deck.show_stack(stack)   
    return (f"Try: {attempts} -> {result}")

print(check_how_many_attemps(deck))