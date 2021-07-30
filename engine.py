import unidecode

# output: utf-8 to ASCII
def secretWord_wout_accents(word):
    return unidecode.unidecode(word, 'utf-8')

def blankLines(word):
    word_as_list = ['_ ' for i in range(len(word))]
    return ''.join([str(char) for char in word_as_list])

# used only if first guess is wrong
def firstAttempt(firstGuess, word):
    word_as_list = [char for char in word]
    if firstGuess not in word_as_list:
        return True

def takingGuess(guess, all_guessed_letters):
    while True:
        if guess in all_guessed_letters:
            guess = input(f'Essa letra já foi usada. Tente uma letra diferente: ').upper()
            guess = guess_wout_accents(guess)
            guess = entryValidation(guess)
        else:
            all_guessed_letters.append(guess)
            break
    return guess, all_guessed_letters

# game = photo of the game on a given moment
def correctGuess(guess, word, game):
    word_as_list = [char for char in word]
    game_as_list = [char for char in game if char != ' ']

    for idx, letter in enumerate(word_as_list):
        if letter == guess:
            game_as_list[idx] = guess

    return ''.join([(f'{str(char)} ') for char in game_as_list])

# output: converts list of wrong guesses to formatted string
def wrongGuessedLetters(wrongGuessedLetters):
    wrong_guesses1 = ''.join([f'{str(char)}, ' for char in wrongGuessedLetters[:-2]])
    wrong_guesses2 = ''.join([f'{str(char)} e ' for char in wrongGuessedLetters[-2:-1]])
    wrong_guesses3 = str(wrongGuessedLetters[-1])
    wrong_guesses = wrong_guesses1 + wrong_guesses2 + wrong_guesses3
    return wrong_guesses

def entryValidation(guess):
    while True:
        if len(guess) == 1 and ((ord(guess) >= 65 and ord(guess) <= 90) or (ord(guess) >= 97 and ord(guess) <= 122)):
            return guess
        else:
            guess = input('O valor informado não é válido. Tente adivinhar apenas uma letra: ').upper()
            guess = guess_wout_accents(guess)

# justification: [entryValidation] uses ASCII which has no accentuated letters
def guess_wout_accents(word):
    return unidecode.unidecode(word, 'utf-8')