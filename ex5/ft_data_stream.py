import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ("Alice", "Dylan", "Bob", "Charlie")
    actions = ("run", "eat", "sleep", "move", "swim")

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        events_list: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    while len(events_list) > 0:
        remove = random.randrange(len(events_list))
        yield events_list.pop(remove)


if __name__ == "__main__":
    g = gen_event()
    for i in range(0, 1000):
        name, action = next(g)
        print(f"Event {i}: Player {name} did action {action}")

    events_list = []
    for _ in range(0, 10):
        events_list.append(next(g))
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")
