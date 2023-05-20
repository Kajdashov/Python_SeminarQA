a = int(input("Введите трехзначное число: "))

if (a >= 100 and a <= 999): 
    result = a // 100 + a // 10%10 + a % 10
    print(result)
else: print("Вы ввели не трехзначное число")