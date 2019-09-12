n = int(input())
counter = 0

for special in range(1111, 9999+1):
    str_special = str(special)
    for num in str_special:
        num = int(num)
        if num == 0:
            continue
        elif n % num == 0:
            counter += 1
            if counter == 4:
                print(special, end=' ')
                counter = 0
    counter = 0