# Дано натуральное число N. Выведите слово YES,
# если число N является точной степенью двойки,
# или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!
# Задача на рекурсию!


def funk(x):
    t = x
    if x % 2 == 0:
        t = int(x / 2)
    elif x % 2 !=0 and x !=1:
        return 'No'
    elif x == 1:
        return 'Yes'

    return funk(t)

print(funk(64))