#В том же проекте создать модуль test_filemanager.py для тестирования функций консольного файлового менеджера
# В файле написать тесты для каждой ""чистой"" функции, чем больше тем лучше. Это могут быть функции консольного файлового менеджера, а так же программы мой счет и программы викторина
#Если в проекте нет функций либо не получается написать ни одного теста, можно использовать мою урезанную версию данного проекта по ссылке: https://yadi.sk/d/n6gyaovRG2
# материалы к занятию:

from homeworks_data import author_info
_programm = filemanager.author_info()

if author_programm ('Leonid Orlov') != 'Leonid Orlov' # ? invalid syntax
print ("Error author_info")


name = input('Введите имя файла')
new_name = input('Введите имя копиии')
filemanager.copy_file_or_directory(name, new_name)

assert filemanager.copy_file_or_directory(name, new_name) == new_name
    print ("Переименование файла- ок") #line 18
    #print ("Переименование файла- ок")
#IndentationError: unexpected indent
# ))) print как проверка функции





