import matplotlib.pyplot as plt
y = [0.596, 0.592, 0.498, 0.728, 0.602, 0.541]

x = []
for n in range(0,len(y)):
    x.append(n+1)
    pass

plt.scatter(x,y)
plt.ylim(0,1)
plt.xlim(0,len(y)+1)
plt.savefig('test.png', dpi=300)
