import matplotlib.pyplot as plt
import numpy as np
#plt.plot([1, 2, 3, 4])
#plt.ylabel('some numbers')
#plt.show()

x = np.linspace(0,5,10)
y = x**2

fig = plt.figure(facecolor='white')

ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(x,y,'r', linewidth=3)
ax1.set_title('parabola')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

ax2 = fig.add_axes([0.2,0.5,0.4,0.3])
ax2.plot(y,x,'g', linewidth=2)
ax2.set_title('sqrt_parabola')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()