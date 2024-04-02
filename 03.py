for _ in range(int(input())):
    n = [int(a) for a in input().split()]
    answer = []
    for ix in input().split():
        if int(ix) > (min(n)+max(n))/2:
            answer.append(ix)
    print(min(n), max(n))
    print(answer)