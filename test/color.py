import numpy as np
np.random.seed(19689801)
import matplotlib.pyplot as plt

x = range(1,11)
y = [9,2,3,4,11,12,5,6,7,8]
color = ['blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green','blue','orange','green']
print(len(x),len(y),len(color))

fig, ax = plt.subplots()
for n in range(0,len(x)):
    #n = 750
    #x, y = np.random.rand(2, n)
    #scale = 200.0 * np.random.rand(n)
    ax.scatter(x[n], y[n], c=color[n], label=color[n],
               alpha=0.3, edgecolors='none')

ax.legend(loc=1)
#ax.grid(True)

plt.show()
plt.savefig('color.png',dpi=300)
