numbers = []
n = int(input("Скільки чисел ви хочете ввести? "))

for i in range(n):
    num = int(input("Введіть число: "))
    numbers.append(num)

target = int(input("Яке число потрібно знайти? "))

count = 0
for num in numbers:
    if num == target:
        count = count + 1

print("Кількість входжень:", count)
