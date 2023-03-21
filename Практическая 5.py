a=int(input("Введите большее основание"))
b=int(input("Введите меньшее основание"))
h=int(input("Введите высоту"))
c=int(float((h*2+((a-b)/2)*2)**(-0.5)))
P=a+b+2*c
print(P)
m=int(input("Введите массу тела"))
V=int(input("Введите объем тела"))
p=m/V
print(p)
a=int(input("Введите первое число"))
b=int(input("Введите второе число"))
c=a+b
d=a*b
e=a-b
print(c, e, d)
N=int(input("Введите колличество жителей"))
S=int(input("Введите площадь государства"))
P=N/S
print(P)
a=int(input("Введите первое ребро"))
b=int(input("Введите второе ребро"))
c=int(input("Введите третье ребро"))
V=a*b*c
S=2*(a*b+b*c+a*c)
print(V, S)
n=int(input("Ввод первого числа"))
m=int(input("Ввод второго числа"))
A=(n+m)/2
B=(n-m)**(1/2)
print (A,B)
n = int(input())
while n > 0: 
    print(n % 10); n //= 10
import math

i=int(input())

a=[int(a) for a in str(i)]

if a[0]+a[1]==a[2]+a[3]:

   print('сумма двух первых цифр РАВНА сумме двух последних цифр')

else:

   print('сумма двух первых цифр НЕ РАВНА сумме двух последних цифр')

if sum(a)%3==0:

   print('сумма цифр кратна 3')

else:

   print('сумма цифр НЕ кратна 3')
a = int(input('Введите трехзначное число '))
s = a // 100;
d = (a - s*100) // 10;
e = a - s*100 - d*10;
b = e*100 + d*10 + s;
r = a - b;
print(r)
v = int(input('Введите трёхзначное число: '))
e = v % 10
v = v // 10
d = v % 10
v = v // 10
s = v % 10
if ((e + d + s) < 100) and ((e+d+s)>10):
   print('Сумма цифр является двухзначным числом')
a = int(input('Введите число а '))
if (e+d+s) % a == 0:
   print('Его сумма кратна числу ', a)
else:
   print('Его сумма не кратна числу ', a)