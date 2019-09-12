n1 = int(input())
n2 = int(input())

counter = 0
even_sum = 0
odd_sum = 0

for i in range(n1, n2+1):
    stringing_i = (str(i))
    for number in stringing_i:
        digit = int(number)
        counter += 1
        if counter % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
        if even_sum == odd_sum and counter == 6:
            print(f'{i} ', end='')
    counter = 0
    even_sum = 0
    odd_sum = 0

