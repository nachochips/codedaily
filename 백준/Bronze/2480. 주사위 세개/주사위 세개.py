def dice_game():
    d1, d2, d3 = input().split()
    d1 = int(d1)
    d2 = int(d2)
    d3 = int(d3)

    if d1 == d2 == d3:
        return 10000 + d1*1000
    elif d1 == d2 or d1 == d3:
        return 1000 + d1*100
    elif d2 == d3:
        return 1000 + d2*100
    elif d1 != d2 != d3:
        return max(d1, d2, d3)*100

print(dice_game())