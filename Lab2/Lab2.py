# вариант 11
x = float(input("Enter x cord: "))    # x - coordinate
y = float(input("Enter y cord: "))	  # y - coordinate

if 	y > x / 2 and pow((x-2),2) + pow(y,2) <= 4:    #перевірка знаходження точки в заштрихованій площині
	print("The point is in an area")
else: print("The point is not in an area")


