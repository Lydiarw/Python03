import random


def gen_player_achievements() -> None:
    print("=== Achievement Tracker System ===")
    titles: list[str] = [
        'Boss Slayer', 'Crafting Genius', 'Collector Supreme',
        'First Steps', 'Master Explorer', 'Sharp Mind',
        'Speed Runner', 'Strategist', 'Survivor', 'Treasure Hunter',
        'World Savior', 'Unstoppable', 'Untouchable'
    ]
    names: list[str] = ['Alice', 'Bob', 'Charlie', 'Dylan']

    p_achievements: list[set[str]] = []
    for n in names:
        value = random.randrange(0, len(titles))
        p_achievements.append(set(random.choices(titles, k=value)))

    for i, name in enumerate(names):
        print(f"Player {name}: {p_achievements[i]}")

    print(f"\nAll distinct achievements: {set(titles)}")

    common_achievements: set[str] = set(p_achievements[0]).intersection(
        *p_achievements[1:]
    )
    print(f"\nCommon achievements: {common_achievements}\n")

    for i, name in enumerate(names):
        achievements = p_achievements[i]
        other_achievements = set().union(
            *(
                p_achievements[j]
                for j in range(len(p_achievements))
                if j != i
            )
        )
        print(f"Only {name} has: {achievements - other_achievements}")

    print('')
    for i, name in enumerate(names):
        print(
            f"{name} is missing: "
            f"{set.difference(set(titles), p_achievements[i])}")


if __name__ == "__main__":
    gen_player_achievements()
