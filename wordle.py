import random
from collections import Counter


frequency_map = dict()
frequency_map_og = dict()


def map_letter_frequency(word):
    
    global frequency_map, frequency_map_og
    word = word.upper()
    frequency_map = Counter(word)
    frequency_map = {letter: count for letter, count in frequency_map.items()}
    frequency_map_og = frequency_map


with open("words.txt", "r") as file:
    five_letter_words = [line.strip() for line in file]


attempt = 1
hidden_word = list((five_letter_words[random.randint(0, len(five_letter_words)-1)]).upper())
not_valid_letters = []
map_letter_frequency("".join(hidden_word))
attempt = 1


while attempt <= 6:


    frequency_map = frequency_map_og.copy()
    guess = list(input("\nEnter your five letter word: ").upper())


    while ("".join(guess)).lower() not in five_letter_words:
        print("That's not a valid word! \n")
        guess = list(input("Enter your five letter word: ").upper())


    boxes = [0]*5
    og_guess= guess.copy()
    not_in_correct_place = []


    for i in range(0, 5):

        if guess[i] == hidden_word[i]:
            boxes[i] = "\U0001F7E9"
            frequency_map[guess[i]] -= 1
            guess[i] = 0


    for i in range(0, 5):

        if guess[i] in hidden_word and frequency_map[guess[i]] > 0:
            boxes[i] = "\U0001F7E8"
            frequency_map[guess[i]] -= 1
            guess[i] = 0
            not_in_correct_place.append(og_guess[i])


    for i in range(0, 5):

        if boxes[i] == 0:
            boxes[i] = "\u274C"

            if og_guess[i] not in hidden_word:
                not_valid_letters.append(og_guess[i])


    if boxes == list("\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"):
        print("Correct guess!")
        break    

    
    else: 
        boxes = "".join(boxes)
        print(f"Your guess: {''.join(og_guess)}")
        print(f"         {(boxes)}" + '\n')

        if len(not_valid_letters) > 0:
            print(f"\nThese letters are not in the word: {set(not_valid_letters)}")
        if len(not_in_correct_place) > 0:
            print(f"These letters are not in the correct place but in the word: {not_in_correct_place}\n")

    attempt += 1
    
    if attempt > 6:
        print(f"The correct word was {''.join(hidden_word)}")


