# 1. В проекте создать новый модуль test_python.py
# 2. В модуле написать тесты для встроенных функций filter, map, sorted, а также для функций из библиотеки math: pi, sqrt, pow, hypot.
import math

def test_filter():
    x_list = [1, 10, 20, -5, 3]
    result_list = [10, 20]
    assert list(filter(lambda y: True if y % 10 == 0 else False, x_list)) == result_list

def test_filter():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = list(filter(lambda x: x % 2 == 0, arr))
    assert arr_f == [2, 4, 6, 8, 0]


def test_map():
    friends = ['max', 'leo', 'mike', 'jane']
    result = ['MAX', 'LEO', 'MIKE', 'JANE']
    assert list(map(lambda y: y.upper(), friends)) == result

def test_map():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr_f = list(map(lambda x: x + 1, arr))
    assert arr_f == [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    

def test_sorted():
    x_list = [1, 10, 20, -5, 3]
    result = [-5, 1, 3, 10, 20]
    assert sorted(x_list) == result

 # число Пи
def test_pi():
    n_pi = math.pi
    assert float(f'{n_pi:.2f}') == 3.14
    assert float(f'{n_pi:.4f}') == 3.1416
    assert float(f'{n_pi:.8f}') == 3.14159265


# квадратный корень неотрицательного числа
def test_sqrt():
    source_list = [1, 4, 9, 16, 64, 1024]
    result_list = [1, 2, 3, 4, 8, 32]
    for i in range(len(source_list)):
        assert math.sqrt(source_list[i]) == result_list[i]
        assert math.sqrt(source_list[i]) ** 2 == source_list[i]
        assert math.sqrt(source_list[i]) * math.sqrt(source_list[i]) == source_list[i]

# возведение в степень
def test_pow():
    x_list = [1, 10, 20, -5, 3]
    y_list = [0, -2, 5, 10, 2]
    for x in x_list:
        for y in y_list:
            assert math.pow(x, y) == x ** y

# гипотенуза угла с катетами x, y
def test_hypot():
    x_list = [1, 2, 3]
    y_list = [3, 4, 5]
    for x in x_list:
        for y in y_list:
            assert math.hypot(x, y) == math.sqrt(x * x + y * y)