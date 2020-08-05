li = []
n = input("enter length : ")
for i in range(1, int(n)):
    k = int(input("enter value : "))
    li.append(k)
pos_nos = list(filter(lambda x: (x > 0), li))
print("Positive numbers in the list: ", *pos_nos)
pos_nos1 = list(filter(lambda x: (x < 0), li))
print("Negative numbers in the list: ", *pos_nos1)
pos_nos2 = list(filter(lambda x: (x == 0), li))
print("zero numbers in the list: ", *pos_nos2)



