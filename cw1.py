numbers = []
n = int(input("Скільки чисел ви хочете ввести? "))

for i in range(n):
    num = int(input("Введіть число: "))
    numbers.append(num)

total = 0
for num in numbers:
    total = total + num

if n > 0:
    average = total / n
else:
    average = 0

print("Сума:", total)
print("Середнє арифметичне:", average)
