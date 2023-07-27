def time_calculator():
    a, b = input().split()
    a = int(a)
    b = int(b)
    cooking_time = int(input())
    mins = cooking_time + b
    if mins >= 60:
        a = a + mins//60
        mins = mins % 60
        if a >= 24:
            a -= 24
        print(a, mins)
    elif mins < 60:
        print(a, mins)

time_calculator()