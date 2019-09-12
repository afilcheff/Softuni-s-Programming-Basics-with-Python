n = input()
num = 0
prime_sum = 0
non_prime_sum = 0

while not n == 'stop':
    num = int(n)
    if num < 0:
        print('Number is negative.')
        num = 0
    if num == 2 or num == 3 or num == 5 or num == 7:
        prime_sum += num
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        non_prime_sum += num
    else:
        prime_sum += num
    n = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')