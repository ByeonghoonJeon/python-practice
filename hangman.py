# Greeting.
# Make a list of word candidate.
# Pick a random word.
# Show as many underbar as letters in the random word.
# Ask "Guess letter"
# Check if input is valid. (No numbers, no more than single letter)
# If input is valid,
# Check if input is in the letter.
# If input is matching to a letter in the random word,
# Remove underbar and show letter(s).
# If input is NOT matching to a letter in the random word,
# Print "You lost one chance and there is n-1 chances left."
# And go to line 5.
# If input is invalid,
# Print "Please input only single letter."
# And go to line 5 again.
import random
import string

print("Welcome to Jeon's Hangman program.")
word_list = [
    "Assignment",
    "Agreement",
    "Argument",
    "Astronaut",
    "Abbreviation",
    "Agriculture",
    "Abusement",
    "Aardvark",
    "Bureaucracy",
    "Beautiful",
    "Bilingual",
    "Beethoven",
    "Circumstance",
    "Chromatography",
    "Chondroitin",
    "Cucumber",
    "Creativity",
    "Chewable",
    "Cooperation",
    "Communication",
    "Colonization",
    "Clarithromycin",
    "Dysphagia",
    "Dimentia",
    "Duplication",
    "Dimension",
    "Denmark",
    "Derivative",
    "Dungeon",
    "Desparado",
    "Ethiopia",
    "Elongation",
    "Erythromycin",
    "Estrogen",
    "Elastinase",
    "Esquire",
    "Electrophoresis",
    "Euphoria",
    "Finalization",
    "Fabulous",
    "Frequency",
    "Feminism",
]

random_word = random.choice(word_list)
len_word = int(len(random_word))
print(" _" * len_word)
while True:
    guess_word = input(f"Guess the {len_word} lettered word!\n")

    while (
        len(guess_word) != 1
        or guess_word in list(string.punctuation)
        or guess_word in list(string.digits)
    ):
        guess_word = input(f"Please input single Alphabet only.\n")

    for guess_word in random_word:
        if guess_word == random_word and (guess_word) == 1:
            print("Matching!")
            continue
        else:
            continue