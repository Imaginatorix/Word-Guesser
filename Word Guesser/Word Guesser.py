print ("Welcome to the Word Guesser")
print ()

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def no_error(letter_2_check, letter_of_lib, place):
    try:
        if letter_2_check == letter_of_lib[place]:
            return True
    except:
        return False

def singular_or_plural(num):
    if num == 1:
        # Singular
        return "word was"
    else:
        # Plural
        return "words were"

def ToOrNotTo_Only(num):
    if num == 1:
        return "Only "
    else:
        return ""

english_words = load_words()

def guess_word():
    print ("Input word to look for (input letters you know, add '_' to the rest)(example: nam_): ")
    print ("PS: This does not work on brand names like Pokemon, etc. and names like Peter, etc.")
    look = input()
    print ()
    len_look = len(look)

    place = 0

    # If not "_", small letter added to all its letters with its proper position
    letter_and_pos = {}
    for letter in look:
        place += 1
        if letter != "_":
            letter_and_pos[place] = letter.lower()

    # print (letter_and_pos)

    possible_words_f1 = []
    possible_words_f2 = []

    # If they have same length, add them to possible_1 // Filter 1
    for word in english_words:
        if len(word) == len_look:
            possible_words_f1.append(word)

    # If they are exactly the same, add them to 2 // Filter 2; last
    for possible_words in possible_words_f1:
        letter_place = 0
        possibility_coin = 0
        for letter in possible_words:
            letter_place += 1
            if no_error(letter, letter_and_pos, letter_place):
                possibility_coin += 1
                if possibility_coin == len(letter_and_pos):
                    possible_words_f2.append(possible_words)

    num_words_found = 0
    for word in possible_words_f2:
        print (word)
        num_words_found += 1

    print ()
    print (f"{ToOrNotTo_Only(num_words_found)}{num_words_found} {singular_or_plural(num_words_found)} found!")
    print ()

guess_word()

running = True
while running:
    ask = input("Would you like to try another one (y/n)? ")
    if ask == "y":
        print ()
        guess_word()
        continue
    elif ask == "n":
        # break
        running = False
    else:
        print ("Please only input either 'y' or 'n'... Please try again.")
        print ()
        continue

print ()
print ("Thank you for using Word Guesser!")