def max_sequence_numbers(*args):
    counter = 1
    max_lenght_seq = 1
    idx = 0

    if len(args):  # Якщо є аргументи
        number = args[0]  # То число, яке має найбільшу довжину ініціалізується як перший аргумент. В подальшому
        # може змінитись
    else:
        return 0, None  # Якщо аргументів в функцію не задали, то повертаємо макс. довж. 0, а число None

    previous = None  # В цій змінній зберігаємо попереднє значення
    for current in args:  # Змінна current відповідає за тепершнє значення

        if (current == previous) :
            counter += 1  # Якщо наступний дорівнює попердньому, то counter інкрементується
        else:
            if counter > max_lenght_seq:  # Якщо довжина теперішньї послідовності більше попередньої довжини
                max_lenght_seq = counter  # То тепер це максимальна довжина послідовності
                number = previous  # Число яке має максимальну послідовність дорівнює попередньому значення

            counter = 1

        previous = current  # Тут поперднє значення буде приймати теперешнє
        idx += 1

    if counter > max_lenght_seq:
        max_lenght_seq = counter
        number = previous

    return max_lenght_seq, number



a = max_sequence_numbers( 1, 2, 3, 4, 4, 4, 4, 4, 4, 5, 6, 7, 4, 2, 2, 5, 5, 5, 5, 5, 5, 5, 5)

print(a)

