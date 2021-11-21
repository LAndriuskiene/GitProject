# Task 1
# Write a program that will convert the sequence of numbers entered by
# the user into text, e.g .:
# 112 -> "one one two"
# 9973 -> "nine nine seven three"
# Hint: you need the input () function, a dictionary and a loop.

numb_dict = {1 : 'one', 2 : 'two', 3: 'three',
             4 : 'four', 5 : 'five', 6 : 'six',
             7 : 'seven', 8 : 'eight', 9: 'nine', 0 : 'zero'}

def convert_numbers_into_text(numbers):
    total =[]
    for num in numbers:
       total.append(numb_dict[int(num)])
    return total

if __name__ == '__main__':

    while True:
        my_number = input('Write some number: ').strip()
        conv = convert_numbers_into_text(my_number)
        print(f'{my_number} --> {" ".join(conv)}')
        shall_continue = input('Continue? Y/N : ')
        if shall_continue.lower() != 'y':
            break



