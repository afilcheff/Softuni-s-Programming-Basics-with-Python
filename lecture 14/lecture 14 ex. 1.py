import sys

n = int(input())
sum_numbers = 0
counter = 0
max_number = -sys.maxsize

for num in range(n):
    num = int(input())
    sum_numbers += num
    if num > max_number:
        max_number = num
    counter += 1
    if counter == n:
        if sum_numbers / 2 == max_number:
            print('Yes')
            print(f' Sum = {max_number}')
        else:
            print('No')
            diff = abs(2 * max_number - sum_numbers)
            print(f'Diff = {diff}')
