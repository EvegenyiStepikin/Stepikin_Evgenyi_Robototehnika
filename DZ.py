temp = int(input("ВВЕДИТЕ ТЕМПЕРАТУРУ (°C): "))
rain = int(input("ЕСТЬ ОСАДКИ? (1/2) 1 - да 2 - нет: "))


if rain == 1 and 30 > temp > 20 :
    print("НАДЕНЬТЕ ФУТБОЛКУ, ШОРТЫ И ВОЗЬМИТЕ ДОЖДЕВИК")

if rain == 2 and 30 > temp > 20 :
    print("НАДЕНЬТЕ ФУТБОЛКУ, ШОРТЫ")
if 20 > temp > 0  :
    level_rain = int(input("ОСАДКИ СИЛЬНЫЕ? (1/2) 1 - да 2 - нет: "))

    if 20 > temp > 0 and rain == 1 and level_rain == 1:
        print("НАДЕНЬТЕ ПАЛЬТО, РЕЗИНОВЫЕ САПОГИ И ВОЗЬМИТЕ ЗОНТ")

    if 20 > temp > 0 and rain == 1 and level_rain == 2:
        print("НАДЕНЬТЕ ПАЛЬТО И ВОЗЬМИТЕ ДОЖДЕВИК")

if temp < 0:
    print("НАДЕНЬТЕ ПУХОВИК")

if 20 > temp > 0  and rain == 2 :
    print("ННАДЕНЬТЕ ПАЛЬТО")