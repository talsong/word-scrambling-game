import random
import urllib.request

def create_permutation(n):
    perm = [-1]*n
    cnt = n
    while cnt:
        index = random.randint(0, n-1)
        if perm[index] == -1:
            perm[index] = cnt - 1
            cnt -= 1
    return perm

def scramble_word(word):
    lst = create_permutation(len(word))
    for i in range(len(lst)):
        lst[i] = word[lst[i]]
    return ' '.join(lst)

word_file = "http://www.desiquintans.com/downloads/nounlist/nounlist.txt" #online compilation of common nouns
reader = urllib.request.urlopen(word_file)
long_text = reader.read().decode()
word_bank = long_text.splitlines()

rand_word = random.choice(word_bank)

def guessing_game():
    word = rand_word.lower()
    scrambled = scramble_word(word)
    while scrambled == word: #check to make sure that the word is not the same
        scrambled = scramble_word(word)
    print("Welcome to Word Scrambler! \nYou have 3 tries to guess the correct word")
    print("type in 'stop game' at any point in order to exit the game")
    print("your word is: ", scramble_word(word))
    for tries in range(3):
        guess = input("Try #" + str(3-tries) + ": ")
        if guess.lower() == "stop game":
            print("Thanks for playing!")
            break
        elif guess.lower() != word:
            print("Try again!")
        else:
            print("Congratulations you guessed the word!")
            return
    if tries == 2:
        print("Sorry, you're out of tries!")
