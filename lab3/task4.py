
num, dep, arr, time, price = input().split(";")

print(f"Поезд: {num}")
print(f"Маршрут: {dep} - {arr}")
print(f"Отправление: {time}")
print(f"Цена: {float(price):.2f} руб")