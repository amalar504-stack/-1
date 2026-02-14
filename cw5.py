numbers = []
n = int(input("Скільки чисел ви хочете ввести? "))

for i in range(n):
    num = int(input("Введіть число: "))
    numbers.append(num)

unique_numbers = []

for num in numbers:
    count = 0
    
    for u in unique_numbers:
        if num == u:
            count = count + 1
    
    if count == 0:
        unique_numbers.append(num)

print("Список без повторів:", unique_numbers)
