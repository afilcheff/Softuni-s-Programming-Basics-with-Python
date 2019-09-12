n = int(input())
p1_c = 0
p2_c = 0
p3_c = 0
counter = 0


for num in range(n):
    num = int(input())
    counter += 1
    if num % 2 == 0:
        p1_c += 1
    if num % 3 == 0:
        p2_c += 1
    if num % 4 == 0:
        p3_c += 1

p1 = p1_c / counter * 100
p2 = p2_c / counter * 100
p3 = p3_c / counter * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')