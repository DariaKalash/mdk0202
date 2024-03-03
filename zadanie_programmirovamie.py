print("Калашниковой Даши мдк02.02. Ниже задание по программированию, хе-хе")
print("Задание А")
def NOD(a, b):
    if a == 0 or b == 0:
        return a + b
    if a > b:
        return NOD( a - b, b )
    else:
        return NOD( a, b - a)
a =  int(input("Введите число "))
b = int(input("Введите число "))
print(NOD(a, b))
