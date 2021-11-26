# Task 6
# Write a function that takes two strings and checks to see if they are
# anagrams of each other.
# For example:
# "Army" and "Mary",
# "Sharing" and "Sunday",
# "Quid est veritas?" and "Vir est qui adest",
# "Jim Morrison" and "Mr. Mojo Risin"
# "Tom Marvolo Riddle" and "I am Lord Voldemort"

def if_anagrams(string1, string2):
    if sorted(string1) == sorted(string2):
        print("Yes, it's Anagramm")
    else:
        print('No, it is not Anagramm')

if __name__ == '__main__':

    while True:

        first_string = input("Enter first string: ")
        second_string = input("Enter second string: ")

        first_string = first_string.lower()
        second_string = second_string.lower()

        first_string = first_string.replace(' ', '')
        second_string = second_string.replace(' ', '')

        answ = if_anagrams(first_string, second_string)

        shall_continue = input('Continue? Y/N : ')
        if shall_continue.lower() != 'y':
            break