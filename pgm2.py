import matplotlib.pyplot as p
x = [1,2,3,4,5]
y = [1,4,9,16,25]
p.figure(1)
p.subplot(221) #for 1 graph
p.grid()
p.plot(x, y, 'ro')
p.subplot(222) #for 2nd figure
p.plot(x, y, 'r--')
p.show()