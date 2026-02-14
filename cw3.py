numbers = []
n = int(input("Скільки чисел ви хочете ввести? "))

for i in range(n):
    num = int(input("Введіть число: "))
    numbers.append(num)

positive_sum = 0
for num in numbers:
    if num > 0:
        positive_sum = positive_sum + num

print("Сума додатних чисел:", positive_sum)
