def is_high_card(cards):
    highest = cards[0]

    for card in cards[1:]:
        if card["value"] > highest["value"]:
            highest = card
    return(highest["label"])

def is_one_pair(cards):
    card_values = [card["value"] for card in cards]

    for i in range(len(card_values)-1):
        for j in range(len(card_values)):
            if card_values[i] == card_values[i+1]:
                return True
    return False

def are_two_pairs(cards):
    card_values = [card["value"] for card in cards]