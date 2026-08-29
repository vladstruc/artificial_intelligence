#Виртуальный кликер (Раздел Функции. Области видимости. Передача параметров в функции")

count = 0

def click():
    global count
    count += 1


def get_count():
    return count


print(get_count())
click()
print(get_count())
click()
print(get_count())
click()
print(get_count())
click()
print(get_count())
click()
print(get_count())
click()
