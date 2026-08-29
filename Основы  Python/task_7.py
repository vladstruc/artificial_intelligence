#Копейка рубль бережёт  (Раздел "Функции. Области видимости. Передача параметров в функции")
list_money = [x for x in input().split()]

def take_small(money):
    new_list_money = []
    for i in range(0, len(money)):
        if (int(list_money[i]) < 100):
            new_list_money.append(list_money[i])
    return new_list_money

print(list_money)
print (take_small(list_money))
