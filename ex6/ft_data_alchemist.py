import random


def comprehension_practice() -> None:
    name: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    all_cap: list[str] = [n.capitalize() for n in name]
    only_cap: list[str] = [n for n in name if n[0].isupper()]
    values: list[int] = []
    for _ in range(len(name)):
        num = random.randrange(1, 1000)
        values.append(num)
    score_dict: dict[str, int] = {n: v for n, v in zip(all_cap, values)}
    average: float = sum(values)/len(name)
    high_dict: dict[str, int] = {
        n: v for n, v in zip(all_cap, values) if v > average
    }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {name}")
    print(f"New list with all names capitalized: {all_cap}")
    print(f"New list of capitalized names only: {only_cap}\n")

    print(f"Score dict: {score_dict}")
    print(f"Score average is {average:.2f}")
    print(f"High scores: {high_dict}")


if __name__ == "__main__":
    comprehension_practice()
