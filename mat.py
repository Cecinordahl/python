from matplotlib import pyplot as plt 
import numpy as np 

V = np.arrange(1, 10, 0.1)
R = 100
I = V / R

plt.title("I/V plot") 
plt.xlabel("Spenning (V)") 
plt.ylabel("Strøm (A)") 
plt.plot(V,I) 
plt.scatter(V,I)
plt.grid()
plt.show()

