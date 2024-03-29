#problem link: https://softuni.bg/trainings/resources/officedocument/39816/exercise-problem-descriptions-programming-basics-with-python-april-2019/2328

max_bad_grades = int(input())

task = input()
bad_grades = 0
problem_count = 0
score = 0
last_task = None

while not task == 'Enough':
    grade = int(input())
    score += grade
    if grade <= 4:
        bad_grades += 1
        if bad_grades >= max_bad_grades:
            print(f'You need a break, {bad_grades} poor grades.')
            break
    problem_count += 1
    last_task = task
    task = input()

Average_score = score / problem_count

if task == 'Enough':
    print(f'Average score: {Average_score:.2f}')
    print(f'Number of problems: {problem_count}')
    print(f'Last problem: {last_task}')
