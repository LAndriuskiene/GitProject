#Task 4
#Create a function that checks that the string given as an argument is a
#palindrome (ie read backwards and forwards is exactly the same, eg
#"kayak", "madam").

def is_palindrom(words):
    if len(words) > 1 and words == words[::-1]:
        return True

if __name__ == '__main__':
    while True:

        my_word = input('Enter your word: ')
        check_word = is_palindrom(my_word)
        if check_word == True:
            print(f"Your word {my_word} is palindrom")
    # print(check_word)
    # if check_word == None:
        else:
            print(f"Your word {my_word} is not palindrom")

        shall_continue = input('Continue? Y/N : ')
        if shall_continue.lower() != 'y':
            break

# word = 'muuu'
# a = is_palindrom(word)
# print(a)