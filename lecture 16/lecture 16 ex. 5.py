n1 = int(input())
n2 = int(input())

counter = 0
sum_1 = 0
sum_2 = 0
number_3 = 0

for i in range(n1, n2+1):
    stringing_i = (str(i))
    for number in stringing_i:
        digit = int(number)
        counter += 1
        if counter <= 2:
            sum_1 += digit
        if counter > 3:
            sum_2 += digit
        if counter == 3:
            number_3 = digit
        diff = abs(sum_1 - sum_2)
        if sum_1 == sum_2 and counter == 5:
            print(f'{i} ', end='')
        elif diff == number_3 and counter == 5:
            print(f'{i} ', end='')

    counter = 0
    sum_1 = 0
    sum_2 = 0
    number_3 = 0

