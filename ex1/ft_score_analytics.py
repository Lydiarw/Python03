import sys

arg = sys.argv[1:]
length = len(arg)
error_msg = (
    f"No scores provided. Usage: python3 {sys.argv[0]} "
    "<score1> <score2> ..."
)

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print(error_msg)
else:
    scores: list[int] = []
    try:
        for score in arg:
            scores.append(int(score))
        print(f"Scores processed: {scores}")
        print(f"Total players: {length}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/length}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError:
        for error in arg:
            print(f"Inavlid paramater: {error}")
        print(f"BOTTOM: {error_msg}")
