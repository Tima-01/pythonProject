def user_number():
    while True:
        x = int(input("Введите число от 1 до 9: "))
        if 1 <= x <= 9:
            return x
        print("Неправильный ввод, попробуйте снова.")


number = user_number()
print(f"Вы ввели: {number}")

if 1 <= number <= 3:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторений для строки: "))
    for i in range(n):
        print(i+1,".",s)
elif 4 <= number <= 6:
    m = int(input("Введите степень числа: "))
    g = number ** m
    print (number, "в степени", m, "=", g)
elif 7 <= number <= 9:
    for i in range(10):
        number += 1
        print(number)
