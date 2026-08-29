#Список покупок (Раздел "Встроенные возможности по работе с коллекциямиы")
from itertools import chain


string_of_shops_1 = input()
string_of_shops_2 = input()
string_of_shops_3 = input()
list_chained = list(chain(string_of_shops_1.split(', '), string_of_shops_2.split(', '), string_of_shops_3.split(', ')))
sorted_list_chained = sorted(list_chained)
for index, name_of_shop in enumerate(sorted_list_chained, start=1):
    print(f"{index}. {name_of_shop}")