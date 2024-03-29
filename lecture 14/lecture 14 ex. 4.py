import sys
n = int(input())
counter = 0
maximum = -sys.maxsize
minimum = sys.maxsize
sum_num = 0

for num in range(2 * n):
    num_1 = float(input())
    num_2 = float(input())
    sum_num += num_1 + num_2
    counter += 1
    if sum_num > maximum:
        maximum = sum_num
    if sum_num < minimum:
        minimum = sum_num
    diff = abs(maximum - minimum)
    if counter == n:
        if sum_num / counter == num_1 + num_2:
            print(f'Yes, value={sum_num}')
        else:
            print(f'No, maxdiff={diff}')