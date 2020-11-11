n = int(input("Input the limit of degrees: "))
tC = 0
tF = 0
print("%6s %6s"%("tC","tF"))
for i in range(0,n+1):
    tC = i
    tF = 9 * tC / 5 + 32
    print("%6d | %5.2f" %(tC,tF),sep="|")