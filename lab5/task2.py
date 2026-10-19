a = int(input())
b = int(input())

total_sum = 0
product = 1

for i in range(a, b + 1):
    total_sum += i
    product *= i

print("Сумма:", total_sum)
print("Произведение:", product)


