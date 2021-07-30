import secretWord as sw
import graphics
import engine

number_of_errors = 0
attempts = 0
all_guessed_letters = []
wrong_guessed_letters = []

secretWord, category, endingWord = sw.secretWord()
word_wout_accents = engine.secretWord_wout_accents(secretWord)
game = engine.blankLines(word_wout_accents)
print(f'\nPalavra secreta: {game}')
graphics.hanging_post(number_of_errors)
guess = input(f'Tente adivinhar uma letra {category}: ').upper()
guess = engine.guess_wout_accents(guess)
guess = engine.entryValidation(guess)
all_guessed_letters.append(guess)
attempts += 1

# output: if user's first guess is wrong, initializes list of wrong guesses
if engine.firstAttempt(guess, word_wout_accents):
    wrong_guessed_letters.append(guess)
    wrong_guesses = engine.wrongGuessedLetters(wrong_guessed_letters)

while True:
    if guess in word_wout_accents:
        game = engine.correctGuess(guess, word_wout_accents, game)
        if '_' not in game:
            print(f'\nParabéns! Você ganhou.\nA palavra secreta era {endingWord}.')
            graphics.hanging_post(number_of_errors)
            break
        print(f'\nTentativa nº {attempts}: Parabéns! Você acertou.\nPalavra secreta: {game}')
        graphics.hanging_post(number_of_errors)

        if len(wrong_guessed_letters) == 1:
            print(f'A letra {wrong_guesses} não está na palavra.')
        elif len(wrong_guessed_letters) > 1:
            print(f'As letras {wrong_guesses} não estão na palavra.')

        if number_of_errors == 4:
            print('Cuidado! Faltam apenas 2 tentativas.')
        elif number_of_errors == 5:
            print('Cuidado! Falta apenas 1 tentativa.')

        guess = input(f'Tente adivinhar uma nova letra {category}: ').upper()
        guess = engine.guess_wout_accents(guess)
        guess = engine.entryValidation(guess)
        guess, all_guessed_letters = engine.takingGuess(guess, all_guessed_letters)
        attempts += 1

    else:
        number_of_errors += 1
        if attempts != 1:
            wrong_guessed_letters.append(guess)
            wrong_guesses = engine.wrongGuessedLetters(wrong_guessed_letters)
        if number_of_errors == 6:
            print(f'\nTentativa nº {attempts}: Você perdeu! A palavra secreta era {endingWord}.\nPalavra secreta: {game}')
            graphics.hanging_post(number_of_errors)
            break
        else:
            print(f'\nTentativa nº {attempts}: Você errou!\nPalavra secreta: {game}')
            graphics.hanging_post(number_of_errors)
                
        if len(wrong_guessed_letters) == 1:
            print(f'A letra {wrong_guesses} não está na palavra.')
        elif len(wrong_guessed_letters) > 1:
            print(f'As letras {wrong_guesses} não estão na palavra.')

        if number_of_errors == 4:
            print('Cuidado! Faltam apenas 2 tentativas.')
        elif number_of_errors == 5:
            print('Cuidado! Falta apenas 1 tentativa.')
        
        guess = input(f'Tente adivinhar uma nova letra {category}: ').upper()
        guess = engine.guess_wout_accents(guess)
        guess = engine.entryValidation(guess)
        guess, all_guessed_letters = engine.takingGuess(guess, all_guessed_letters)
        attempts += 1  