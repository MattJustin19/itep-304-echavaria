# itep-304-echavaria


m = float(input('Enter first side: '))
a = float(input('Enter second side: '))
t = float(input('Enter third side: '))


s = (m + a + t) / 2


area = (s * (s - m) * (s - a) * (s - t)) ** 0.5
print('The area of the triangle is %0.2f' % area)
