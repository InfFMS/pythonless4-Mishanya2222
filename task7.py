# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
def funk(x, y, z):
    if x+y<z and x + z < y and z + y < x:
        print(True)
    else:
        print(False)
    return "досвидания"
print(funk(int(input()), int(input()), int(input())))