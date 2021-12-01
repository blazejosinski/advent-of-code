from itertools import islice
from collections import deque
from helpers import read_grouped_lines

def winner_score(deck):
    return sum([a*b for a,b in zip(deck, range(len(deck), 0, -1))])


def normal_combat(filename):
    groups = read_grouped_lines(filename)
    decks = [deque([int(a) for a in g[1:]]) for g in groups]
    
    while decks[0] and decks[1]:
        cards = [d.popleft() for d in decks]
        winner = cards.index(max(cards))
        decks[winner].append(max(cards))
        decks[winner].append(min(cards))
    
    winner_deck = decks[0] if decks[0] else decks[1]
    return winner_score(winner_deck)
    

def recurse_combat_winner(decks):
    played_decks = set()
    while decks[0] and decks[1]:
        winner = -1
        tupled = tuple(tuple(d) for d in decks)
        if tupled in played_decks:
            return 0
        played_decks.add(tupled)
        cards = [d.popleft() for d in decks]
        if winner == -1:
            if cards[0] > len(decks[0]) or cards[1] > len(decks[1]):
                winner = cards.index(max(cards))
            else:
                recursive_decks = [deque(islice(d, c)) for c, d in zip(cards, decks)]
                winner = recurse_combat_winner(recursive_decks)
        decks[winner].append(cards[winner])
        decks[winner].append(cards[1-winner])
    return 0 if decks[0] else 1


def recursive_combat(filename):
    groups = read_grouped_lines(filename)
    decks = [deque([int(a) for a in g[1:]]) for g in groups]
    winner = recurse_combat_winner(decks)    
    return winner_score(decks[winner])


def main():
    # print(normal_combat("in251"))
    # print(normal_combat("in25"))
    print(recursive_combat("in251"))
    print(recursive_combat("in25"))


if __name__ == "__main__":
    main()