n = int(input())
odd_count = 0

for r in range(n):
    current_c = 1
    row_text = ""

    for k in range(r + 1):
        if k == 0:
            row_text += str(current_c)
        else:
            row_text += " " + str(current_c)

        if current_c % 2 != 0:
            odd_count += 1

        if k < r:
            current_c = current_c * (r - k) // (k + 1)

    print(row_text)
print("Нечетных элементов:", odd_count)

