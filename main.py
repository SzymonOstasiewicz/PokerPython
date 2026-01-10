from deck import Deck
from hand import *
import time

deck = Deck() 
deck.shuffle()
stack = deck.draw_stack(5)

# deck.show_stack(stack)
print()

HANDS = {
    10: {"name": "ROYAL FLUSH",    "count": 0},
    9:  {"name": "STRAIGHT FLUSH", "count": 0},
    8:  {"name": "QUADS",          "count": 0},
    7:  {"name": "FULL HOUSE",     "count": 0},
    6:  {"name": "FLUSH",          "count": 0},
    5:  {"name": "STRAIGHT",       "count": 0},
    4:  {"name": "THREE OF A KIND","count": 0},
    3:  {"name": "TWO PAIRS",      "count": 0},
    2:  {"name": "PAIR",           "count": 0},
    1:  {"name": "HIGH CARD",      "count": 0}
}

def check_the_hand(stack):
    if (is_royal_flush(stack)):
        return 10
    if (is_straight_flush(stack)):
        return 9
    if (is_Quads(stack)):
        return 8
    elif (is_full_house(stack)):
        return 7
    elif (is_flush(stack)):
        return 6
    elif (is_straight(stack)):
        return 5
    elif (is_three_of_kind(stack)):
        return 4
    elif (are_two_pairs(stack)):
        return 3
    elif (is_one_pair(stack)):
        return 2
    else: return 1

def count_reset(HANDS):
    for hand in HANDS:
        HANDS[hand]["count"] = 0

def check_how_many_attemps(deck):
    attempts = 0
    start = time.time()

    while True:
        attempts += 1
        deck.reset()
        stack = deck.draw_stack(5)

        hand = check_the_hand(stack)
        HANDS[hand]["count"] += 1
  
        if hand == 10:
            end = time.time()
            print(f"Czas wykonywania sie programu: {round(end - start, 3)}s\n")  
            return attempts
            

def print_stats(attempts):
    for strength in sorted(HANDS, reverse=True):
        print(f"{HANDS[strength]["name"]}: -> {HANDS[strength]["count"]} | {round(HANDS[strength]["count"]*100/attempts, 3)}%")
    print(f"\nall attemps was: {attempts}")

count_reset(HANDS)
attempts = check_how_many_attemps(deck)
print_stats(attempts)
# Funckja pokazująca jaki jest wynik rozgrywki
# def check_the_hand(stack):
#     if (is_royal_flush(stack)):
#         return "ROYAL FLUSH!"
#     if (is_straight_flush(stack)):
#         return "STRAIGHT FLUSH!"
#     if (is_Quads(stack)):
#         return "QUADS!"
#     elif (is_full_house(stack)):
#         return "FULL HOUSE!"
#     elif (is_flush(stack)):
#         return "FLUSH!"
#     elif (is_straight(stack)):
#         return "STRAIGHT!"
#     elif (is_three_of_kind(stack)):
#         return "THREE OF A KIND!"
#     elif (are_two_pairs(stack)):
#         return "TWO PAIRS!"
#     elif (is_one_pair(stack)):
#         return "PAIR!"
#     else: return is_high_card(stack)

# print(check_the_hand(stack))

