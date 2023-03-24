#1
s1 = int(input('Введите расстояние в километрах')) 
s2 = int(input('Введите расстояние в метрах')) 
t1 = int(input('Введите время в часах')) 
t2 = int(input('Введите время в минутах')) 
speed1 = s1 // t1 #скорость в километрах в час 
speed2 = s2 // t2 * 3.6 #скорость в мертрах в секунду 
if speed1 > speed2: 
 print('Скорость 1 больше скорости 2 ') 
else: 
 print('Скорость 1 меньше скорости 2 ')

#2
radius = int(input('Введите радиус круга')) 
kvadrat = int(input('Введите длинну стороны квадрата')) 
ploshad1 = 3.14 * radius * radius 
ploshad2 = kvadrat * kvadrat 
if ploshad1 > ploshad2: 
 print('площадь круга больше площади квадрата') 
else: 
 print('площадь круга меньше площади квадрата')

#3

num1 = input() 
num2 = input() 
if num1 > num2: 
 max = num1 
 min = num2 
else: 
 max = num2 
 min = num1 
print('Большее число -',max, 'Меньшее число -',min)

#4
stsquare = int(input()) 
radius = int(input()) 
diametr = radius * 2 
if stsquare >= diametr: 
 print('Впишется') 
else: 
 print('Не впишется')

#5
e = int(input("Введите трехзначное число"))
if e>1000:
  print("Ошибка")
r = e//100
t = e%100
y = t//10
u = t%10
o= u*100+y*10+r
print("Ответ",e-o)
