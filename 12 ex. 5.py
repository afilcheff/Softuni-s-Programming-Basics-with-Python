
change = float(input())

counter = 0

change = int(change * 100)

while not change == 0:
    if change // 200 > 0:
        change -= 200
    elif change // 100 > 0:
        change -= 100
    elif change // 50 > 0:
        change -= 50
    elif change // 20 > 0:
        change -= 20
    elif change // 10 > 0:
        change -= 10
    elif change // 5 > 0:
        change -= 5
    elif change // 2 > 0:
        change -= 2
    elif change // 1 > 0:
        change -= 1
    counter += 1

if change == 0:
    print(counter)