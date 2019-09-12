n = int(input())
counter = 0

for num in range(1, n+1):
    for row in range(1, num + 1):
        counter += 1
        print(f'{counter} ', end='')
        if counter == n:
            break
    print()
    if counter == n:
        break
