#find the prime number between m and n
m=100
n=300
print("Prime numbers between", m, "and", n, "are:")
for n1 in range(m,n+1):
   if n1 > 1:
       for i in range(2, n1):
           if (n1 % i) == 0:
               break
       else:
           print(n1)