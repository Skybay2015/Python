import math

a = input('Первый катет: ')
b = input('Второй катет: ')

print("Гипотенуза:", round((math.sqrt(int(a) ** 2 + int(b) ** 2)), 2))
