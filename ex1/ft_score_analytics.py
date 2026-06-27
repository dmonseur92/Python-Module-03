import sys


def print_scores() -> None:
    scores = [0] * (len(sys.argv) - 1)
    count = 0
    i = 1
    while i < len(sys.argv):
        try:
            scores[count] = int(sys.argv[i])
            count += 1
        except (ValueError, TypeError):
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    scores = scores[:count]
    if len(scores) == 0:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)} ")
    print(f"Average score: {sum(scores)/len(scores)} ")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("===  Player Score Analytics  ===")
    print_scores()
