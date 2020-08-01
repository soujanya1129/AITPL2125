#finding largest of 3 nos using functions
def largest(x,y,z):
    if(x>=y) and (x>=z):
        large=x
    elif(y>=x) and (y>=z):
         large=y
    else:
         large=z
    return large

x=1000
y=1589
z=3456
print(largest(x,y,z))
