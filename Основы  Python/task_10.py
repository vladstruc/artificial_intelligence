#Анализ качества образовательной программы (Раздел "Базовые конструкции Python")

N, M, Q, cw, sw, hw, tw = map(int, input().split())
dict_of_raitings = {}
if (N >= 3 and M >= 0 and all(x > 0 for x in (cw, sw, hw, tw)) is True):
    for i in range(0, N):
        prev_a = 0
        prev_b = 0
        prev_c = 0
        prev_d = 0
        raiting = 0
        student_lastname = input("Введите фамилию студента")
        for j in range(0, M):
            a, b, c, d = map(int, input().split())
            a = prev_a + a
            b = prev_b + b
            c = prev_c + c
            d = prev_d + d
            prev_a = a
            prev_b = b
            prev_c = c
            prev_d = d
            raiting = (a*cw+b*sw+c*hw+d*tw)
            dict_of_raitings[student_lastname] = raiting
            max_raiting_int = max(dict_of_raitings.values())
    if (max_raiting_int > Q):
        print("Ошибка в вводе данных!")
    else:
        dict_of_raitings = {key: round((value/Q)*100) for key, value in dict_of_raitings.items()}    
        max_raiting = max(dict_of_raitings.values())
        avg_raiting = round(sum(dict_of_raitings.values())/len(dict_of_raitings))
        min_raiting = min(dict_of_raitings.values())
        print(f"Максимальный рейтинг: {max_raiting}, Средний рейтинг: {avg_raiting}, Минимальный рейтинг: {min_raiting}")
        top_three = sorted(dict_of_raitings.items(), key = lambda x: x[1], reverse = True) [:3]
        for i, (student, raiting) in enumerate(top_three, start=1):
            print(f"{student} {raiting}% (top-{i})")
        if (avg_raiting <= 50):
            print("Курс усваивается плохо")
        else:
            print("Курс усваивается хорошо")
else:
    print("Ошибка в вводе данных!")




    



