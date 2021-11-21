#Task 3
#Create a function that checks that the number given in the argument is
#prime. The function should take a numeric value and return a logical
#value of True / False.
#E.g.
#For 11 the function will return True, for 12 -> False

def if_number_prime(numb):
    count = 0
    for i in range(1, numb+1):
        if numb % i == 0:   # tikrinu ar mano skaicius dalinasi is skaiciu: 1,2,3...num
            count +=1
    if count != 2:          # paprastas skaicius dalinasi is 1 ir pacio
        return False
    return True

if __name__ == '__main__':

    while True:
        my_number = int(input("Please, input any number: "))
        is_prime = if_number_prime(my_number)
        if is_prime is True:
            print('True')
        else:
            print('False')

        shall_continue = input('Continue? Y/N : ')
        if shall_continue.lower() != 'y':
            break

