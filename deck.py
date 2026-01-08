import random;

Color = ['♥️','♦️',
         '♣️', '♠️']
Ranks = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']
RANK_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
class Deck:
    def __init__(self):
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        cards = []
        for color in Color:
            for rank in Ranks:
                cards.append({
                    "rank": rank,
                    "color": color,
                    "value": RANK_VALUES[rank],
                    "label": f"{rank}{color}"
                })
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def show_cards(self):
        for card in self.cards:
            print(card["label"])

    def reset(self):
        self.cards = self.create_deck()
        self.shuffle()

    def draw_card(self):
        return self.cards.pop(random.randrange(len(self.cards)))
        
    def draw_stack(self, amount):
        stack = []
        for _ in range(amount):
            stack.append(self.draw_card())
        return stack
    
    def show_stack(self, stack):
        print("  | ".join(card["label"] for card in stack))

    def sort_cards(cards):
        card_values = [card["value"] for card in cards]

        for _ in range(len(card_values)):
            for j in range(len(card_values)-1):
                if card_values[j] < card_values[j+1]:
                    tmp = card_values[j]
                    card_values[j] =  card_values[j+1]
                    card_values[j+1] = tmp
        return card_values