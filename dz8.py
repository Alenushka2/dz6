import os
import sys
from os import listdir
from os.path import isfile, join
import random, shutil

while True:
    print('1. создать папку вводит название папки')
    print('2. удалить(файл / папку)')
    print('3. копировать(файл / папку)')
    print('4. просмотр содержимого  рабочей директории')
    print('5. посмотреть только папки)')
    print('6. посмотреть только файлы)')
    print('7. просмотр информации об операционной системе)')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский  счет')
    print('11.смена рабочей директории')
    print('12.выход')
    choice = input('Выберите пункт меню:')
 # после выбора пользователь вводит название папки, создаем её в рабочей директории
    if choice == '1':
        print("*" * 40)
        print()
        answer = input('Укажите имя создаваемой директории -> ')
        temp_dir = os.path.join(os.getcwd(), answer)
        print("Указанная директория уже существует. Укажите другое имя") if os.path.exists(temp_dir) else os.mkdir(temp_dir), print("Директория успешно создана")
        print()
        print("*" * 40)
    elif choice == '2':
        print("*" * 40)
        print()
        answer2 = input('Укажите имя файла или папки для удаления -> ')
        for answer2 in sys.path:
            d_answer2 = os.getcwd()
            for answer2 in d_answer2:
                shutil.rmtree (answer2)
            print("Удаление no успешно") if not os.path.exists(answer2) else print("Указанный файл/директория не найдена в текущей директории")
        print()
        print("*" * 40)
    elif choice == '3':
        def copy_file():
            source = input('Вводим имя файла для копирования: ')
            destination = input('Вводим  имя папки куда копируем: ')
            if source == destination:
                 print("Исходное имя папки совпадает с конечным именем.  Введите другое имя.")
            if source != destination:
                source = os.path.join(os.getcwd(), source)
                destination = os.path.join(os.getcwd(), destination)
                if os.path.exists(source):
                     # если копируем файл, если директория -> директорию
                    shutil.copy(source, destination), print("скопировали Файл  ", destination) if os.path.isfile(source) else os.path.isdir(source), shutil.copytree(source, destination), print("скопировали каталог")
                return destination
        copy_file()
    elif choice == '4':
        print("*" * 40)
        print()
        path = input("Ведите путь для проверки содержимого директории (если текущей, то введите ""t"": ")
        path = os.getcwd(), print(os.listdir(path)) if path == 't' else print('Ведите путь для проверки содержимого другой директории')
        print()
        print("*" * 40)

    elif choice == '5':
        path = input("Ведите путь для поиска папок: . ") #input .
        d = '.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        print(folders)

    elif choice == '6':
        print("*" * 40)
        print()
        from viev_files import onlyfiles
        print(*onlyfiles)
        print()
        print("*" * 40)

    elif choice == '7':
        print("*" * 40)
        print()
        print(sys.platform)
        print()
        print("*" * 40)

    elif choice == '8':
        print("*" * 40)
        print()
        print("Elena")
        print()
        print("*" * 40)

    elif choice == '9':
        #  correct_answer = ca
        #  incorrect_answer = ia
        # date figures = df
        # date letters = dl
        # famous people = fp
        import random

        famous_dataset = [
            {'fp': 'А.С.Пушкин', 'df': '06.06.1799', 'dl': '6 июня 1799 г.'},
            {'fp': 'Т. Эдисон', 'df': '11.02.1847', 'dl': '11 февраля 1847 г.'},
            {'fp': 'Н. Тесла', 'df': '10.07.1856', 'dl': '7 июля 1856 г.'},
            {'fp': 'К. Э. Циолковский', 'df': '17.09.1857', 'dl': '28 сентября 1857 г.'},
            {'fp': 'С.П. Королёв', 'df': '12.01.1907', 'dl': '12 января 1907 г.'},
            {'fp': 'Януш Корчак', 'df': '22.07.1878', 'dl': '22 июля 1878 г.'},
            {'fp': 'А. С. Макаренко', 'df': '13.03.1888', 'dl': '13 марта 1888 г.'},
            {'fp': 'М. Шичида', 'df': '08.09.1929', 'dl': '8 сентября 1929 г.'},
            {'fp': 'Л. Костенко', 'df': '19.03.1930', 'dl': '19 марта 1930 г.'},
            {'fp': 'С. М. Фёдоров', 'df': '08.08.1927', 'dl': '8 августа 1927 г.'}
        ]
        famous_count = 5
        famous_for_test = random.sample(famous_dataset, famous_count)
        correct_answer = 0
        incorrect_answer = 0

        wish_play = True
        some_counts = 0

        while wish_play:
            for fp in famous_for_test:
                user_answer = input(f'Введите дату рождения человека {fp["fp"]} , в формате "день.месяц.год"')
                if user_answer == fp["df"]:
                    print(random.sample(['Точно!', 'Отлично!', 'Великолепно!', 'Правильно!'], 1)[0])
                    correct_answer += 1
                else:
                    print(random.sample(['Не совсем так :(', 'Почти :(', 'Ошибочка :(', 'Мимо :('], 1)[0])
                    incorrect_answer += 1
                    print(f'Правильный ответ: {fp["dl"]}')
            print("*" * 40)
            print()
            print(f'Верно отвечено на {correct_answer / famous_count * 100}% и неверно отвечено на {incorrect_answer / famous_count * 100}% от заданных вопросов.')
            print()
            print("*" * 40)
            # счетчик попыток
            some_counts += 1
            wish_play = input('Чтобы попытаться еще раз введите "да", для выхода введите что-нибудь другое :D')
            wish_play = True if wish_play == 'да' else wish_play = False
        print(f'Благодарим за участие в викторине!')

    elif choice == '10':
        bill_sum = 0
        history = []
        def buy(bill_sum):
            cost = int(input('Enter purchase cost'))
            if cost > bill_sum:
                print('There is not enough money in the account')
            else:
                bill_sum -= cost
                name = input('Enter purchase name:')
                history.append((name, cost))
            return bill_sum


        while True:
            print('1. refill')
            print('2. purchase')
            print('3. exit')

            choice = input('Select menu item:')
            if choice == '1':
                cost = int(input('Enter amount'))
                bill_sum += cost
            elif choice == '2':
                bill_sum = buy(bill_sum)
            elif choice == '3':
                break
            else:
                print('Invalid menu item')

    elif  choice == '11':
        print("*" * 40)
        print()
        path = input("Введите директорию: ") # input .
        if path == '.':
            os.chdir(path)
        print()
        print("*" * 40)

    elif choice == '12':
        break
    else:
        print('Неверный пункт меню!')