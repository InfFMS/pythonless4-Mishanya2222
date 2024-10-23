# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7
g = list()
def funk(x):
    if x == 1:
        return
    t = x
    for i in range(2, x+1):
        if x % i == 0:
            g.append(i)
            break
    funk(t//i)
funk(int(input()))
print(print(g))