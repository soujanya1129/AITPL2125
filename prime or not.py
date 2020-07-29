#prime or not
n1=67
if n1> 1:
    for i in range(2, n1):
        if (n1 % i) == 0:
            print( "not  prime number")
            break
    else:
        print("prime number")
else:
    print("not prime number")