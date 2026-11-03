n = int(input())
if n < 2:
    print("Не простое")
else:
    d = 2
    is_prime = True

    while d * d <= n:
        if n % d == 0:
            is_prime = False
            break
        d += 1

    if is_prime:
        print("Простое")
    else:
        print("Не простое")
