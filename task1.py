# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
def funk(x)
    g=0
    for I in range(1, x):
        g=g+1
        print("*"*g)

print(int(input()))
