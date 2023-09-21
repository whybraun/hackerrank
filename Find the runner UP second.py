if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)

    unique_scores = list(set(scores))

    unique_scores.sort(reverse=True)

    second_scores = unique_scores[1]

    print(second_scores)