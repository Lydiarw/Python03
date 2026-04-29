from typing import Generator
import random


def gen_event() -> Generator[tuple[str, str], None, None]:
    name_list: list[str] = ['alice', 'bob', 'charlie', 'dylan']
    action_list: list[str] = [
        'climb', 'eat', 'grab', 'move',
        'release', 'run', 'sleep', 'swim'
    ]
    while True:
        name = random.choice(name_list)
        action = random.choice(action_list)
        chosen = (name, action)
        yield chosen


def consume_event(
        event_list: list[tuple[str, str]]
        ) -> Generator[list[tuple[str, str]], None, None]:
    while True:
        pick = random.choice(event_list)
        print(f"Got event from list: {pick}")
        event_list.remove(pick)
        yield event_list


def data_stream() -> None:
    g: Generator[tuple[str, str], None, None] = gen_event()
    # ^^^^ create ONE generator
    for num in range(1000):
        name, action = next(g)
        print(f"Event {num}: Player {name} did action {action}")

    event_list: list[tuple[str, str]] = []
    h: Generator[tuple[str, str], None, None] = gen_event()
    for num in range(10):
        name, action = next(h)
        event_list.append((name, action))
    print(f"Built list of 10 events: {event_list}")

    c: Generator[list[tuple[str, str]], None, None] = consume_event(event_list)
    for i in range(10):
        updated_list = next(c)
        print(f"Remains in list: {updated_list}")


if __name__ == "__main__":
    data_stream()

# next(gen_event) = next(function)
# next(g) = next(generator instance)
