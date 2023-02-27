a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
discret = b**2 - 4*a*c
# <<b**2>> возведение b в квадрат
print("Дискриминант = " + str(discret))
if discret < 0:
    print("Корней нет")
elif discret = 0:
    x = -b / (2 * a)
    print("x =" + str(x))
else:
    x1 = (-b + discret ** 0.5) / (2 * a)
    x2 = (-b - discret ** 0.5) / (2 * a)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))