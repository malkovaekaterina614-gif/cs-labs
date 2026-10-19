summ = 0
c=0

while True:
    vvod = input()
    if vvod == "stop":
        break
    cena = int(vvod)
    summ = summ + cena
    c += 1
if c == 0:
    print("Нет покупок")
else:
    srednyaya = summ / c

    print("Покупок:", c)
    print("Общая стоимость:", summ, "руб")
    print(f"Средняя стоимость: {srednyaya:.2f} руб")


