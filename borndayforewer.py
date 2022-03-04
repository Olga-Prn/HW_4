"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def victory_writer(writer_name, **kwargs):
    """
    для запуска викторины введите папраметры key --> value
    key - год или день
    value - значение года или для
    writer_name - имя писателя
    """
    for key, value in kwargs.items():
        if key == 'год':
            year = int(input('Ввведите год рождения {} : '.format(writer_name)))
            while year != value:
                print("Не верно")
                year = int(input('Ввведите год рождения {} : '.format(writer_name)))
            print('Верно')
        elif key == 'день':
            day = int(input('Ввведите день рождения {} : '.format(writer_name)))
            while day != value:
                print("Не верно")
                day = int(input('В какой день июня родился {} : '.format(writer_name)))
            print('Верно')
        pass
victory_writer(writer_name = 'А.С. Пушкина', год = 1799, день = 6)
