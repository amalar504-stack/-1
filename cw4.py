numbers = []
n = int(input("Скільки чисел ви хочете ввести? "))

for i in range(n):
    num = int(input("Введіть число: "))
    numbers.append(num)

print("Індекси парних чисел:")

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        print(i)
