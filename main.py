tseloe = 10
drobnoe = 8.4
stroka = "No"

tseloe = tseloe * 3.5

big_netseloe = tseloe - 1.0

ab = tseloe / drobnoe
с = big_netseloe / drobnoe

stroka = stroka * 2 + "Yes" * 3


print(ab)
print(tseloe)
print(drobnoe)
print(tseloe)
print(big_netseloe)
print(drobnoe)
print(с)
print(stroka)

a=1
b=3
print((a>b)and (b<a))
print((b>a)and (b<a))
print ((a>b)and(b>a))
print(not(b>a))
c = a+b
print((c>b)or (b>a))
print((a>c)or (b>c))
print ((c<b)or(b<a))
print((a<c) or (b>a))
e ='Nasos'
w = 'Nos'
print((e>w) and (w>e))
print((w>e)or (w < e))
print(not(e<w))

dark = input("Вы хотите спать(Да,Нет, Не знаю)")
if dark == "Да":
    print("Идите сать")
elif dark =="Не знаю":
    print ("Подумайте ещё")
else:
    print("Идите гулять")