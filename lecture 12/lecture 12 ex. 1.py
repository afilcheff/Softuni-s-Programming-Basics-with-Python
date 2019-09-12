fav_book = input()
capacity = int(input())

book = input()
counter = 0

while not fav_book == book:

    counter += 1
    if counter >= capacity:
        print(f'The book you search is not here !')
        print(f'You checked {counter} books.')
        break

    book = input()

if fav_book == book:
    print(f'You checked {counter} books and found it.')
