#problem link: https://softuni.bg/trainings/resources/officedocument/39816/exercise-problem-descriptions-programming-basics-with-python-april-2019/2328

trip_cost = int(input())
money = float(input())

action = None
income = 0
days_counter = 0
spend_counter = 0

while not money >= trip_cost:
    action = input()
    if action == 'save':
        money += float(input())
        days_counter += 1
        spend_counter = 0
    else:
        money -= float(input())
        if money <= 0:
            money = 0
        spend_counter += 1
        days_counter += 1
        if spend_counter >= 5:
            print(f"You can't save the money.")
            print(days_counter)
            break

if money >= trip_cost:
    print(f'You saved the money for {days_counter} days.')
