import random;

Color = ['♥️','♦️',
         '♣️', '♠️']
Ranks = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.cards = []

        for color in Color:
            for rank in Ranks:
                self.cards.append({
                    "rank": rank,
                    "color": color,
                    "label": f"{rank} {color}"
                })

    def shuffle(self):
        random.shuffle(self.cards)

    def show_cards(self):
        for card in self.cards:
            print(card["label"])
    
    def get_random_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
        
    def draw_stack(self, amount):
        stack = []
        for _ in range(amount):
            stack.append(self.get_random_card())
        return stack
        
