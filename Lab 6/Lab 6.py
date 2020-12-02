# варіант 20

def gX(x):
    if x != 0:
        x_num_1 = x_num_0 = x
        x_div_1 = x_div_0 = 1
        numerator = x_num_1
        divider = x_div_1
        for k in range(1,11):
            # calculating numerator
            x_num_0 = x_num_1
            x_num_1 = x_num_0 * pow(x, 2) / ((2 * k) * (2 * k + 1)) # recurrent formula of sum of numerator
            numerator += x_num_1

            # calculating divider
            x_div_0 = x_div_1
            x_div_1 = x_div_0 * pow(x, 3) / ((3 * k) * (3 * k - 1) * (3 * k - 2)) # recurrent formula of sum  of divider
            divider += x_div_1
        result = numerator / divider
        return result
    print("Argument of function g(x) cant be 0")
    quit()
y = float(input("Input y:"))
main_result = (1.7 * gX(0.25) + 2 * gX(1 + y)) / (6 - gX(pow(y,2)-1))
print("Output:", "%8.6f" % main_result)