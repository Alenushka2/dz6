#В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
#Если в проекте нет функций либо не получается написать ни одного теста, можно использовать мою урезанную версию данного проекта по ссылке: https://yadi.sk/d/n6gyaovRG2 - да, данные по этой ссылке поместила в homeworks_data.py

#создала переменную
author_programm = input('Введите имя автора программы')
name = ('Leonid Orlov')
# проверяю эту переменную:
if author_programm  != name:
    print ("Error author_info")



# соответствие месяца и его названия
months = {
    '01': 'январь',
    '02': 'февраль',
    '12': 'декабрь'
}
klient_answer = input('Введите название зимнего месяца:')
assert klient_answer in months

# py- test
from victory1 import famous_people , famous_dataset
def test_famous_people():
    assert user_answer in famous_dataset