# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.




def zachem_tut_funkciya(a,b):
    t = 1
    for i in range(1,max(a,b)):
        if a % i==0 and  b%i==0:
            g = i
            t=t*g
    return t
print(zachem_tut_funkciya(int(input()),int(input())))