#Task 2
#Create a function that takes a list of integers and returns what the
#smallest number is in.
#Do not use built-in functions.
#eg for the list [42, 13, 56, 7, 12, 3, 85] the function should return 5, because
#the smallest element is found at this index in this list.

def smallest_number_index(number_list):
    minimal_number = min(number_list)
    result = number_list.index(minimal_number)
    return result


if __name__ == '__main__':

    while True:
        my_list = [int(x) for x in input('Ivesk skaiciu seka per kableli: ').split(',')]
        # my_list = [42, 13, 56, 7, 12, 3, 85]
        min_elem = smallest_number_index(my_list)
        print(min_elem)
        shall_continue = input('Continue? Y/N : ')
        if shall_continue.lower() != 'y':
            break




