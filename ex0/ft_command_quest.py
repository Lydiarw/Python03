import sys

arg: list[str] = sys.argv
length: int = len(arg)
i: int = 1

print("=== Command Quest ===")
print(f"Program name: {arg[0]}")
if length <= 1:
    print("No arguments provided!")
if length > 1:
    print(f"Arguments received: {length - 1}")
    while i < length:
        print(f"Argument {i}: {arg[i]}")
        i += 1
print(f"Total arguments: {i}")
