#Task 5
#Create a function that will calculate the number of upper and lower case
#letters in a string.
#eg for: "The quick Brown Fox"
#expected result:
#Number of uppercase letters: 3, number of lowercase letters : 13
#Hint: use a loop, conditional statement, and appropriate methods for the
#string

def count_upper_lower_letters(string):
    count_u = 0
    count_l = 0
    for letter in string:
        if (letter.isupper()) == True:
            count_u +=1
        elif (letter.islower()) == True:
            count_l +=1
    print(f"Number of uppercase letters: {count_u}")
    print(f"Number of lowercase letters: {count_l}")

if __name__ == "__main__":

    my_string = input("Enter your string: ")
    letters_number = count_upper_lower_letters(my_string)