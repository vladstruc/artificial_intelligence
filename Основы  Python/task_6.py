#Средний рост (Раздел "Потоковый ввод/вывод. Работа с текстовыми файлами. JSON")
from sys import stdin

lines = []
heights_prev = []
heights_now = []

for line in stdin:
    lines.append(line.rstrip("\n"))

for i in range(0, len(lines)):
    heights_prev.append(int(lines[i].split(' ')[1]))
    heights_now.append(int(lines[i].split(' ')[2]))


avg_of_heights_prev = sum(heights_prev) / len(heights_prev)
avg_of_heights_now = sum(heights_now) / len(heights_now)


difference = round(avg_of_heights_now - avg_of_heights_prev)

print(difference)
