import random


def gen_player_achievements() -> None:
    achievements = (
        "Keyboard Warrior", "Vanilla Vim addict", "Segfault King",
        "Infinite Loop Lover", "2x Split choker", "AI Copy Ninja",
        "TIG enjoyer", "Empty repo Emperor", "Charlie Kirk OS Destroyer",
        "Strlen failer", "Norminette Junkie", "Kahoot feedback bomber"
    )

    players: dict[str, set] = {
        "Alice": set(),
        "Bob": set(),
        "Charlie": set(),
        "Dylan": set()
    }

    for name in players:
        nb = random.randint(4, 8)
        players[name] = set(random.sample(achievements, nb))
        print(f"Player {name}: {players[name]}")
        print()
    print(f"All distinct achievements: {set.union(*players.values())}\n")
    print(f"Common achievements : {set.intersection(*players.values())}\n")

    for name in players:
        others = set().union(*(players[n] for n in players if n != name))
        print(f"Only {name} has: {players[name].difference(others)}")
    print()

    for name in players:
        print(f"{name} is missing:"
              f"{set(achievements).difference(players[name])}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
