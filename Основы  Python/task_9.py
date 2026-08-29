#Странная игра (Раздел "Функции. Области видимости. Передача параметров в функции")

count = 0


def move(name, number):
    global count
    if name == 'Петя':
        count += number
    elif name == 'Ваня':
        count -= number


def game_over():
    if count > 0:
        return "Петя"
    elif count < 0:
        return "Ваня"
    elif count == 0:
        return "Ничья"


move('Петя', 3)
move('Ваня', 4)
move('Петя', 4)
move('Ваня', 3)
print(game_over())

