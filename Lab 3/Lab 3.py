
b = 1        #поточний член послідовності
a = 0        #попередній член
x = float(input("Input x: "))
n = 0
s = b        #сума послідовності
e = 1e-4


while abs(b-a) >= e:
    print("b-a: %8.6f" % (b-a))
    a = b
    b = a * (-1) * x**2 / ((( 2 * n ) + 1) * ( 2 * n + 2))   #обчислення поточного члена
    print("\ta:%11.7f" % a)
    print("\tb:%11.7f" % b)
    n += 1
    s+=b
    print("\ts: %8.5f" % s)
print("Final sum:%7.5f"%s)