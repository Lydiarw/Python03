import math


def parse_coordinates(user_input):
    parts = user_input.split(',')
    if len(parts) != 3:
        print("Invalid syntax")
        return
    c_list = []
    for n in parts:
        try:
            c_list.append(float(n))
        except ValueError:
            print(
                f"Error on parameter '{n}': could not convert string "
                f"to float: '{n}'"
            )
            return
    tuple1 = tuple(c_list)
    return (tuple1)


def get_coordinates():
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        tuple1 = parse_coordinates(user_input)
        if tuple1 is not None:
            return (tuple1)


def get_player_pos():
    print("=== Game Coordinate System ===")

    ordinal = ['first', 'second']
    all_coords = []
    for order in ordinal:
        print(f"\nGet a {order} set of coordinates")
        coords = get_coordinates()
        print(f"Got a {order} tuple: {coords}")
        x, y, z = coords  # unpacking the tuple
        print(f"It includes: X={x}, Y={y}, Z={z}")
        all_coords.append((x, y, z))
        print(f"Distance to center: {round(math.sqrt(x**2 + y**2 + z**2), 4)}")
    (x1, y1, z1), (x2, y2, z2) = all_coords
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(
        f"\nDistance between the 2 sets of coordinates: {round(distance, 4)}"
    )


if __name__ == "__main__":
    get_player_pos()
