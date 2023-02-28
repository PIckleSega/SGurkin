a = int(input('Введите трёхзначное число '))
b = a
c = 0
if 99<a<1000:
 while (a>0):
    d = a % 10
    c = c * 10 + d
    a = a // 10
 if (c == b):
    print("Это палиндром")
 else:
    print("Это не палиндром")
else:
   print('Число не трёхзначное')