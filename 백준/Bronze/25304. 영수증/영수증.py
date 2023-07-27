def receipt():
    total = int(input())
    n_items = int(input())
    total_sum = 0

    for i in range(n_items):
        p, q = input().split()
        p = int(p)
        q = int(q)
        pq = p * q
        total_sum += pq

    if total == total_sum:
        print("Yes")
    else:
        print("No")

receipt()