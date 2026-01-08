def is_high_card(cards):
    highest = cards[0]

    for card in cards[1:]:
        if card["value"] > highest["value"]:
            highest = card
    return (f"HIGHEST CARD: {highest["label"]}")

def count_occurrences(cards):
    card_values = [card["value"] for card in cards]
    occurrences = 0
    
    for i in range(len(card_values)-1):
        for j in range(i+1, len(card_values)):
            if card_values[i] == card_values[j]:
                occurrences += 1
    if (occurrences) > 0: return occurrences
    else: return 0

def is_one_pair(cards):
    if(count_occurrences(cards) == 1): return True

def are_two_pairs(cards):
    if(count_occurrences(cards) == 2): return True

def is_three_of_kind(cards):
    if(count_occurrences(cards) == 3): return True

def is_full_house(cards):
    if(count_occurrences(cards) == 4): return True

def is_Quads(cards):
    if(count_occurrences(cards) == 6): return True
