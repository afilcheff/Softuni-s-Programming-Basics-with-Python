n = int(input())
name = input()
profit = 0
profit_interim = 0
profit_per_fish = 0
counter = 0

while not name == 'Stop':
    for i in range(1, n+1):
        for letter in name:
            letter = ord(letter)
            if i % 3 == 0:
                profit_interim += letter
            else:
                profit_interim -= letter
        kilos = float(input())
        profit_per_fish = profit_interim/kilos
        profit += profit_per_fish
        profit_interim = 0
        if i == n:
            print('Lyubo fulfilled the quota!')
            break
        name = input()
        if name == 'Stop':
            break
    break

if profit > 0:
    print(f"Lyubo's profit from {i} fishes is {profit:.2f} leva.")
else:
    profit = abs(profit)
    print(f'Lyubo lost {profit:.2f} leva today.')