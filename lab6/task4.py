n = int(input())
if n < 0:
    print("Ошибка")
else:
    count = 0
    total = 0
    if n == 0:
        count = 1
    else:
        while n > 0:
            digit = n % 10
            total += digit
            count += 1
            n //= 10

    print("Цифр:", count)
    print("Сумма цифр:", total)

