n = int(input())
sum_grades = 0
presentation = input()
final_grade = 0
counter = 0

while not presentation == 'Finish':
    for i in range(n):
        grade = float(input())
        sum_grades += grade
    average_grade = sum_grades / n
    final_grade += average_grade
    print(f'{presentation} - {average_grade:.2f}.')
    counter += 1
    sum_grades = 0
    presentation = input()

final_grade = final_grade / counter
print(f"Student's final assessment is {final_grade:.2f}.")