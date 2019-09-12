n = int(input())
b = int(input())
q = b + 97
maximum = 0

for line1 in range(1, n+1):
    for line2 in range(1, n+1):
        for line3 in range(97, q):
            for line4 in range(97, q):
                maximum = 0
                if line1 > maximum:
                    maximum = line1
                if line2 > maximum:
                    maximum = line2
                for line5 in range(maximum, n+1):
                    if line5 > maximum:
                        print(f'{line1}{line2}{chr(line3)}{chr(line4)}{line5} ', end='')
                        