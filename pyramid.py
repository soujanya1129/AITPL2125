#program to demonstrate pyramid of nos
rows=8
for row in range(1,rows):
    for column in range(row,0,-1):
        print(column,end=' ')
    print(""" """)
