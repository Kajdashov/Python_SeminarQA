# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#   3 2 4 -> yes
#   3 2 1 -> no

n,m,k = int(input('Введите количество долек 1-й стороны (n): ')),\
        int(input('Введите количество долек 2-й стороны (m): ')),\
        int(input('Введите количество долек которое вы хотите отломить (k): '))

if(k%n == 0 or k%m == 0):
    print(f"От Вашей шоколадки можно отломить кусок = {k} долек")
else: print("От Вашей шоколодки нельзя отломить прямоугольный кусочек")