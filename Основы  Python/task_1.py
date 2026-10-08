#Анонс новости (Раздел "Строки, кортежи, списки")
L = int(input())
N = int(input())
titles = []
for i in range(0, N):
    title = str(input())
    titles.append(title)
for i in range(0, N):
    if (len(titles[i]) <= L):
        print(titles[i])
    else:
        print(f"{titles[i][:L-3]}...")
