#Task 7
#Write a function that will return the 5 most common words from
#Mickiewicz's work. https://pastebin.com/raw/aAHeW5Pt (copy and save
#to a text file what you will find at this link).
#Hint: use the open() function, split() method, dictionary and loop.

def most_common_words(words_text):
    word_count = dict()
    for word in words_text:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    a = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:5]  # rusiuojam pagal values
                                                                          # mazejimo tvarka ir imam 5 didziausias reiksmes
    print(a)


if __name__ == '__main__':

    with open('words.txt', 'r', encoding="utf-8") as text_file:
        my_text = text_file.read()

    my_text = my_text.split()
    common = most_common_words(my_text)