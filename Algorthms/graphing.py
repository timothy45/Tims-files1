import matplotlib.pyplot as plt

y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

plt.bar(x,y)
plt.show()
