from bs4 import BeautifulSoup
import requests
from googletrans import Translator


translator = Translator()


def get_english_words():
    url = 'https://randomword.com'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        return {
            "english_words": english_word,
            "word_definition": word_definition
        }
    except:
        print('Произошла ошибка')


def word_game():
    print('Игра началась')
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word = translator.translate(word, src='en', dest='ru').text
        word_definition = word_dict.get("word_definition")
        word_definition = translator.translate(word_definition, src='en', dest='ru').text

        print(f'Значение слова - {word_definition}')
        user = input('Что это за слово? ')
        if user == word:  # Сравниваем без учета регистра
            print('Правильно')
        else:
            print(f'Неправильно, правильное слово - {word}')
        play_again = input('Хотите сыграть еще? y/n: ')
        if play_again != 'y':
            print('Игра окончена')
            break


word_game()