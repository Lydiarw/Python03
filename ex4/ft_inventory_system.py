import sys


def parse_args(argv: list[str]) -> dict[str, int] | None:
    inventory: dict[str, int] = {}
    if len(argv) < 2:
        print('Please input more than one argument')
        return None
    for a in argv[1:]:
        try:
            item, qty = a.split(':')
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue
            try:
                inventory[item] = int(qty)
            except ValueError:
                print(
                    f"Quantity error for '{item}': invalid literal for "
                    f"int() with base 10: '{qty}'"
                )
        except ValueError:
            print(f"Error - invalid parameter '{a}'")
    return inventory


def display_inventory() -> None:
    print('=== Inventory System Analysis ===')

    inventory = parse_args(sys.argv)
    if inventory is None:
        return
    key_list = list(inventory.keys())
    total_value = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {key_list}")
    print(f"Total quantity of the {len(inventory)} items: {total_value}")
    for item, qty in inventory.items():
        print(f"Item {item} represents {qty/total_value:.1%}")
    print(
        f"Item most abundant: {max(inventory, key=lambda k: inventory[k])} "
        f"with quantity {max(inventory.values())}"
    )
    print(
        f"Item least abundant: {min(inventory, key=lambda k: inventory[k])} "
        f"with quantity {min(inventory.values())}"
    )
    inventory.update({'magic_item': 1})
    print(f"Update inventory: {inventory}")


if __name__ == "__main__":
    display_inventory()

# key= : for each key, run this func & compare the results
# lambda func runs for each key:
# inventory["apple"] -> 5
# inventory["orange"] -> 2
# compares the results and find max/min
# inventory[k] is the return value
