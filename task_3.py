#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
# Без использования встроенной функции преобразования, без строк.

def translation(x, y):
    result = []
    while x != 0:
        result.append(x % y)
        x = x//y
    result.reverse()
    return result
number = int(input("Введите число:  "))
razrayd = 2
print(*translation(number, razrayd))