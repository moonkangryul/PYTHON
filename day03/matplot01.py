import matplotlib.pyplot as plt

x= [1,4,9,16,25,36,49,64]
# plt.plot(x)
# plt.show()

y = [i for i in range(1,9)]
plt.plot(x,y)
plt.xlabel(x)
plt.ylabel(y)
plt.title('matplotlib sample')


y1 = [13,24,54,4,5,12,14]
plt.plot(y1)
plt.show()