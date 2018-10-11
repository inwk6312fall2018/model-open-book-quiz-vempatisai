import pyCardDeck
from pyCardDeck.cards import PokerCard

def number_of_cards():
  card_list=[]
  french_suit = ["Hearts","Spades","Clubs","Diamonds"]
  map= {'A':'Ace','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','J':'Jack','Q':'Queen','K':'King'}
  for item in french_suit:
    for map,value in map.item():
      card_list.append((item,value))
  print('total number of cards on the table')

class Poker:
  def __init__(self, members):
    self.members = list(range(1,members))
    self.deck = pyCardDeck.Deck(cards=generate_initial_deck(),name='Poker Game',reshuffle=False)
    self.table_cards=[]
    self.hand = []
    print("This is a poker table with {} members"%d(members))

  def texas_holdem(self):
    print("Starting a round of Texas Hold'em")
    self.deck.shuffle()
    self.draw_cards(2)

  def draw_cards(self, number):
    card = []
    for _ in range(0, number):
      for player in self.players:
        card = self.deck.draw()
	player.append(card)
      print("Dealt {} to player {}"%d(card, player))

    return cards

print(number_of_cards())
P = PokerTable(5)
print(P.draw_cards(5))
