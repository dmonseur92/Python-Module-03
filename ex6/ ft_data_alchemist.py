import random

def comprehensions()-> None:
    players = ("Alice", "dylan", "Bob", "charlie", "Emma", "Gregory", "john", "kevin", "Liam")
    players_all_caps = [player.capitalize() for player in players]
    players_og_caps = [player for player in players if player == player.capitalize()]
    scores = {player: random.randint(0, 1000) for player in players_all_caps}
    av_score = float(sum(scores.values()) / len(scores))
    scores2 = {player: score for player, score in scores.items() if score > av_score}
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_all_caps}")
    print(f"New list of capitalized names only:: {players_og_caps}")
    print(f"Score dict: {scores}")
    print(f"Score average is {round(av_score, 2)}")
    print(f"High scores: {scores2}")

if __name__=="__main__":
    print("=== Game Data Alchemist ===\n")
    comprehensions()