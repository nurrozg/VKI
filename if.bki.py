
name = input('ad: ')
weight = float(input('kilo : '))
length = float(input('boy : '))
index= weight / length **2
if (index >= 0) and (index <= 18.4 ):
    print(f'{name} kilo indeksiniz {index} zayıf olan aralıktasınız ')
elif (index>18.4) and (index<=24.9):
    print(f'{name} kilo indeksiniz {index} normal olan aralıktasınız')
elif(index >= 25.0) and ( index <= 29.9):
    print(f'{name} kilo indeksiniz {index} fazla kilolu olan aralıktasınız')
elif(index >= 30.0) and ( index <= 34.9): 
     print(f'{name} kilo indeksiniz {index} obez olan aralıktasınız')
else:
     print('bilgileriniz yanlış.')