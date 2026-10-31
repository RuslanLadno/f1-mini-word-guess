from random import randint
word_list = ["феррари", "леклер", "хэмилтон", "быки", "ферстаппен", "хаджар", "мерседес",
            "антонелли", "рассел", "макларен", "норрис", "пиастри",
            "алонсо", "чемпион", "болид", "пилот", "подиум", "трасса",
            "финиш", "монако", "сузука", "монца", "боттас", "сайнс",
            "албон", "гасли", "окон", "стролл", "поул", "шина", "гонка", "шумахер", "феттель",
            "росберг", "баттон", "райконнен"]
def get_word():
    s = randint(0, len(word_list)-1)
    return word_list[s].upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
                ''',
                # голова, торс, обе руки
                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
                ''',
                # голова, торс и одна рука
                '''
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
                ''',
                # голова и торс
                '''
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                ''',
                # голова
                '''
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                ''',
                # начальное состояние
                '''
                --------
                |      |
                |      
                |    
                |      
                |     
                -
                '''
    ]
    return stages[tries]

# print(display_hangman(0))


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Давайте играть в угадайку слов на тематику формулы 1!')
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries > 0:
        letter = input('Какую ты хочешь ввести букву? Или сразу назовёшь слово?\n').upper()
        new_word = ''
        if len(letter) == 1 and letter.isalpha():
            if letter not in guessed_letters:
                guessed_letters.append(letter)
                for i in word:
                    if i in guessed_letters:
                        new_word += i
                    else:
                        new_word += '_'
                word_completion = new_word
            else:
                print('Эту букву ты уже назвал. Назови другую букву или целое слово\n')
                continue
            if letter not in word:
                tries -= 1
                print(f'Такой буквы нет. У тебя осталось {tries} попыток')
            print(display_hangman(tries))
            print(new_word)
            if '_' not in new_word:
                guessed = True


        elif len(letter) > 1 and letter.isalpha():
            if letter in guessed_words:
                print('Такое слово уже было названо. Попробуй ещё раз.')
                continue
            elif letter == word:
                guessed_words.append(letter)            
                guessed = True
            else:
                guessed_words.append(letter)
                tries -= 1
                print(display_hangman(tries))
                print(f'Слово названо неправильно. У тебя осталось {tries} попыток')
                print(word_completion)
        else:
            print('Некорректный ввод, попробуйте ещё раз.')

    if guessed:
        print(f'Поздравляем, вы угадали слово {word}! Вы победили!')
    else:
        print(f'Попытки закончились, правильное слово {word}')


while True:
    play(get_word())
    replay = input('Ты хочешь ещё раз сыграть в игру? (Если да, отправь +, если нет, отправь -)\n').strip()
    if replay == '-':
        print('Спасибо, что сыграл, заходи ещё!')
        break
        



