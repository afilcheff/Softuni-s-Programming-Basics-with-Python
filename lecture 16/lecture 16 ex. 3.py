n = int(input())
stuff = reversed(str(n))

for number in stuff:
    new = int(number) + 33

    if number == '0':
        print('ZERO', end='')
    else:
        m = int(number)
        for times in range(m):
            print(chr(new), end='')
    print()
