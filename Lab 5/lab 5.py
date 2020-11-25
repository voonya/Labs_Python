# варіант 7

for i in range(1,1001):
    x = i           #копія згенерованого числа
    reverseX = 0    #обернене до згенерованого число
    modX = 0        #остання цифра числа
    while x > 0:
        modX = x % 10
        x = x // 10
        reverseX = reverseX * 10 + modX
    if reverseX == i:
        print("%4d" % i)