import random

def secretWord():
    while True:
        category = input('Digite a categoria desejada: [F]rutas, [P]aíses, [A]nimais ou [O]bjetos: ')
        if category.upper() in ['F', 'P', 'A', 'O']:
            break
        else:
            while True:
                category = input('Digite apenas a primeira letra da categoria desejada: ')
                if category.upper() in ['F', 'P', 'A', 'O']:
                    break
        break

    if category.upper() == 'F':
        file = 'lista_frutas.txt'
        category = 'da fruta'
    elif category.upper() == 'P':
        file = 'lista_paises.txt'
        category = 'do país'
    elif category.upper() == 'A':
        file = 'lista_animais.txt'
        category = 'do animal'
    elif category.upper() == 'O':
        file = 'lista_objetos.txt'
        category = 'do objeto'

    # choose secret word according to category
    with open(file, 'r', encoding='utf-8') as file:
        list_of_words = file.readlines()
        formatted_words = [word.strip().upper() for word in list_of_words]
        secretWord = random.choice(formatted_words)
    
    # formatted secret word
    if category == 'do país':
        endingWord = secretWord.lower().capitalize()
    else:
        endingWord = secretWord.lower()

    return secretWord, category, endingWord