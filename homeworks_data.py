#filemanager
import shutil
import os
import sys


def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def filenames():
    result = []
    for item in os.listdir():
        if os.path.isfile(item):
            result.append(item)
    return result


def author_info():
    return 'Leonid Orlov'


def quit():
    sys.exit(0)


 # main
"""
Модуль для запуска консольного файлового менеджера
"""

# Функции файлового менеджера
import filemanager
# Мой счет
from bill import run_bill
# Викторина
from victory import run_victory

# Названия пунктов меню
COPY_FILE_FOLDER = 'Копировать (файл/папку)'
SHOW_FILES = 'Посмотреть только файлы'
AUTHOR = 'Создатель программы'
VICTORY = 'Играть в викторину'
BILL = 'Мой банковский счет'
EXIT = 'Выход'

# Набор пунктов меню
menu_items = (
    COPY_FILE_FOLDER,
    SHOW_FILES,
    AUTHOR,
    VICTORY,
    BILL,
    EXIT
)


def separator(count=30):
    """
    Функция разделитель
    :param count: количество звездочек
    :return: красивый разделитель
    """
    return '*' * count


def copy_file_or_folder():
    """
    Копирование файла или папки
    :return:
    """
    # спрашиваем имя и новое имя
    name = input('Введите имя файла')
    new_name = input('Введите имя копиии')
    # копируем
    filemanager.copy_file_or_directory(name, new_name)


def print_author():
    """
    Функция печати информации об авторе
    :return:
    """
    # получаем информацию
    author = filemanager.author_info()
    # печатаем
    print(author)


def print_files():
    """
    Функция печати файлов в рабочей папке
    :return: None
    """
    # Получаем файлы
    files = filemanager.filenames()
    # Выводим
    for item in files:
        print(item)


# Словарь действия связывает название пункта меню с той функцией которую нужно выполнить
actions = {
    COPY_FILE_FOLDER: copy_file_or_folder,
    SHOW_FILES: print_files,
    AUTHOR: print_author,
    VICTORY: run_victory,
    BILL: run_bill,
    EXIT: filemanager.quit
}


def print_menu():
    """
    Функция вывода меню
    :return: None
    """
    print(separator())
    # Выводим названи пункта меню и цифру начиная с 1
    for number, item in enumerate(menu_items, 1):
        print(f'{number}) {item}')
    print(separator())


def is_correct_choice(choice):
    """
    Функция проверяет что выбран корректный пункт меню
    :param choice: выбор
    :return: True/False
    """
    return choice.isdigit() and int(choice) > 0 and int(choice) <= len(menu_items)


if __name__ == '__main__':
    # цикл основной программы
    while True:
        # рисуем меню
        print_menu()
        # пользователь выбирает цифру
        choice = input('Выберите пункт меню ')
        # проверяем что это корректный выбор
        if is_correct_choice(choice):
            # получаем назвнание пункта меню по номеру
            # choice - 1, т.к. в меню пункты выводятся с 1 а в картеже хранятся с 0
            choice_name = menu_items[int(choice) - 1]
            # получаем действие в зависимости от пунктам меню
            action = actions[choice_name]
            # вызываем функцию
            action()
        else:
            print('Неверный пункт меню')


#victory
import random

# соответствие месяца и его названия
months = {
    '01': 'января',
    '02': 'февраля',
    '06': 'июня'
}

# соответствие дня и его названия
days = {
    '01': 'первое',
    '02': 'второе',
    '03': 'третье',
    '04': 'четвертое',
    '12': 'двенадцатое',
    '26': 'двадцать шестое'
}

# словарь известных людей и из дат рождения
FAMOUS = {
    'А.С. Пушкин': '26.06.1799',
    'Авраам Линкольн': '12.02.1809',
    'Анджелина Джоли': '04.06.1975'
}


def date_to_str(date):
    """
    Функция приводит дату к текстовому виду
    :param date: дата в формате dd.mm.yyyy
    :return: дата в текстовом виде
    """
    day, month, year = date.split('.')
    result = f'{days[day]} {months[month]} {year} года'
    return result


def run_victory():
    """
    Функция запуска игры викторина
    :return:
    """
    is_play = True
    while is_play:
        # брем 2х из 3х известных людей (только их имена)
        random_famous = random.sample(list(FAMOUS.keys()), 2)
        # идем по именам
        for item in random_famous:
            # просим ввести дату рождения
            answer = input(f'Дата рождения {item} в формате dd.mm.yyyy ')
            # получаем правильный ответ
            true_answer = FAMOUS[item]
            # сравниваем
            if answer == true_answer:
                print('Верно')
            else:
                print('Неверно')
                # получаем дату в текстовом виде
                correct_answer = date_to_str(true_answer)
                # выводим
                print(f'Правильный ответ: {correct_answer}')

        play_again = None
        # Будем спрашивать пока не ответят Да или Нет
        while play_again not in ('Да', 'Нет'):
            play_again = input('Хотите поиграть еще (Да/Нет)? ')

        # Да - продолжаем, Нет - выходим
        is_play = play_again == 'Да'

#bill
"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""


def run_bill():
    """
    Функция запускает программу личный счет
    :return:
    """
    bill_sum = 0
    history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cost = int(input('Введите сумму'))
            bill_sum += cost
        elif choice == '2':
            cost = int(input('Введите сумму покупки'))
            if cost > bill_sum:
                print('Недостаточно средств')
            else:
                bill_sum -= cost
                name = input('Введит название покупки')
                history.append((name, cost))
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')