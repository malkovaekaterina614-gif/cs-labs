# правильность команды  пользователя
def is_valid_command(command):
    # (указано в задании при каких условиях и что)
    if command == "0" or command == "1" or command == "2" or command == "exit":
        return True
    else:
        return False

# Функция проверяет, хватает ли топлива на выбранную мощность двигателя
def can_burn(power, fuel):
    # Если текущего топлива больше или столько же, сколько требует мощность — возвращаем True
    if fuel >= power:
        return True
    else:
        return False

# Функция рассчитывает один шаг полета и возвращает новые значения
def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    # 1. Тратим топливо на величину мощности двигателя
    new_fuel = fuel - power

    # 2. Считаем новую скорость: старая скорость + гравитация - торможение двигателя
    new_speed = speed + gravity - (thrust_step * power)

    # Если скорость ушла в минус, приравниваем её к нулю по условию задачи
    if new_speed < 0:
        new_speed = 0

    # 3. Считаем новую высоту: вычитаем новую скорость из текущей высоты
    new_height = height - new_speed

    # Если высота ушла в минус, касание поверхности
    if new_height < 0:
        new_height = 0
    # Возвращаем тройку новых значений (кортеж)
    return new_height, new_speed, new_fuel


# Функция определяет, закончился ли полет и с каким результатом
def get_status(height, speed, safe_speed=2):
    # Если высота больше нуля — модуль всё еще летит
    if height > 0:
        return "В полете"

    # Если высота 0 и скорость не превышает безопасную (2) — это мягкая посадка
    if height == 0 and speed <= safe_speed:
        return "Посадка успешна"

    # Если высота 0, но скорость слишком большая — это крушение
    if height == 0 and speed > safe_speed:
        return "Авария"


def format_state(height, speed, fuel):
    return "Высота: " + str(height) + " | Скорость: " + str(speed) + " | Топливо: " + str(fuel)


def main():
    height = 36
    speed = 3
    fuel = 10
    gravity = 3
    thrust_step = 4
    # Выводим самое стартовое состояние модуля на экран
    print(format_state(height, speed, fuel))

    # Бесконечный цикл игры, пока модуль не приземлится или пользователь не выйдет
    while True:
        command = input()
        # Проверяем, существует ли вообще такая команда
        if is_valid_command(command) == False:
            print("Ошибка команды")
            continue
        if command == "exit":
            print("Полет прерван")
            break

        power = int(command)
        # Проверяем, хватает ли топлива на этот шаг
        if can_burn(power, fuel) == False:
            print("Недостаточно топлива")
            continue
        # Вызываем симуляцию шага и перезаписываем переменные состояния
        height, speed, fuel = simulate_step(height, speed, fuel, power, gravity, thrust_step)
        print(format_state(height, speed, fuel)) # Выводим на экран обновившиеся после шага параметры
        status = get_status(height, speed) # Проверяем текущий статус полета
        # Если статус изменился и мы больше не "В полете" — выводим результат и завершаем игру
        if status != "В полете":
            print(status)
            break

# Точка входа: запускает функцию main(), если файл запущен напрямую
if __name__ == "__main__":
    main()
