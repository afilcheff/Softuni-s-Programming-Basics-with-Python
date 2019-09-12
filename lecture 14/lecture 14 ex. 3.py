import sys

n = int(input())

counter = 0
odd_sum = 0
even_sum = 0
odd_max_number = -sys.maxsize
odd_min_number = sys.maxsize
even_max_number = -sys.maxsize
even_min_number = sys.maxsize
even_counter = 0
odd_counter = 0

for num in range(1, n + 1):
    num = float(input())
    counter += 1
    if counter % 2 == 0:
        even_sum += num
        even_counter += 1
        if num > even_max_number:
            even_max_number = num
        if num < even_min_number:
            even_min_number = num
    else:
        odd_sum += num
        odd_counter += 1
        if num > odd_max_number:
            odd_max_number = num
        if num < odd_min_number:
            odd_min_number = num

if odd_counter > 0:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin={odd_min_number:.2f},')
    print(f'OddMax={odd_max_number:.2f},')
else:
    print(f'OddSum={odd_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')

if even_counter > 0:
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min_number:.2f},')
    print(f'EvenMax={even_max_number:.2f}')
else:
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')