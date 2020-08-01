#write a python program to find whether a number is positive negative or zero
n = int(input("Enter a number: "))
if n > 0:
    print("{0} is a positive number".format(n))
elif n == 0:
    print("{0} is zero".format(n))
else:
    print("{0} is negative number".format(n))
