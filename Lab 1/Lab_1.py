b = float(input("Введіть перший член прогресії: "))            #Введення першого члена проресії b
if b:
    q = float(input("Введіть знаменник прогресії: "))          #Введення знаменника прогресії q
    if q > -1 and q!=0 and q < 1:
        s = (b / (1-q))                                        #Обчислення суми прогресії
        print(round(s,4))                                               
    else: print("Error. Знаменник не може дорівнювати нулю або прогресія не є спадною")
else: print("Error. Перший член не може дорівнювати нулю") 

