from matplotlib import pyplot as plt 

U=[0, 1, 2, 3]
I=[0, 0.02, 0.04, 0.06]

plt.title("I/V plot") 
plt.xlabel("Voltage (V)") 
plt.ylabel("Current (A)") 
plt.plot(U,I) 
plt.scatter(U,I)
plt.grid()
plt.show()