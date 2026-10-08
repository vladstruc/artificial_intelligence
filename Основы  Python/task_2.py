#Очистка данных  (Раздел "Строки, кортежи, списки")
list_of_strings = []
while True:
    line = input()
    if (line == ""):
        break
    else:
        if line.endswith("@@@") is False: 
            if line.startswith("##") is True:
                line = line.strip('##')
            list_of_strings.append(line)
for i in range(0, len(list_of_strings)):
    print(list_of_strings[i])
