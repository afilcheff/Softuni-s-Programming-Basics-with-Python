name = input()

grade = 1
result = 0

while grade <= 12:
    score = float(input())

    if score >= 4:
        result += score
        grade += 1

av_score = result / 12
print(f'{name} graduated. av grade: {av_score:.2f}')
