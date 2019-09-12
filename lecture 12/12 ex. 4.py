# link to ex: https://softuni.bg/trainings/resources/officedocument/39816/exercise-problem-descriptions-programming-basics-with-python-april-2019/2328

steps = 0
action = input()

while not action == 'Going home':
    steps = steps + int(action)
    if steps > 10000:
        print('Goal reached! Good job!')
        break
    action = input()

if action == 'Going home':
    steps += int(input())
    if steps < 10000:
        diff = 10000 - steps
        print(f'{diff} more steps to reach goal.')
    else:
        print(f'Goal reached! Good job!')
