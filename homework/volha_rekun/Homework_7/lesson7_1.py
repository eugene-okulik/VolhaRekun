# Задание №1 - "Угадайка"
# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.

# Подсказка: задание выполняется с помощью цикла while

ugadaj = 4

while True:
    user_input = int(input('Введите цифру:'))
    if user_input == ugadaj:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
